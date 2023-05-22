from telegram.ext import CommandHandler, MessageHandler, Application, ContextTypes, filters
import os
from dotenv import load_dotenv
import logging
from telegram import Update
from utils import get_pokemon_name

load_dotenv()

token = os.environ.get("API_KEY")

# Función para manejar el comando "/start"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ingrese el ID del Pokémon a buscar")
    context.user_data['next_step'] = 'handle_pokemon_id'

# Función para manejar el comando "/hello"
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# Función para manejar la respuesta del usuario con el ID del Pokémon
async def handle_pokemon_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = update.message.text  # Obtener el mensaje del usuario
    pokemon_id = message_text.strip()  # Obtener el ID del Pokémon ingresado
    pokemon_name = get_pokemon_name(pokemon_id)  # Obtener el nombre del Pokémon
    if pokemon_name:
        link = f'https://pokemon.gameinfo.io/es/pokemon/{pokemon_id}-{pokemon_name}'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=link)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No se encontró un Pokémon con ese ID")

# Función para manejar los mensajes del usuario
async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if 'next_step' in context.user_data:
        next_step = context.user_data['next_step']
        del context.user_data['next_step']
        if next_step == 'handle_pokemon_id':
            await handle_pokemon_id(update, context)

# Configurar el bot
def main():
    # Configurar el registro de errores
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.ERROR)

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('hello', hello))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))

    application.run_polling()

if __name__ == '__main__':
    main()
