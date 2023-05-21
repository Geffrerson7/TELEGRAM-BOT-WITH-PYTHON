from telegram.ext import CommandHandler, Application, ContextTypes
import os
from dotenv import load_dotenv
import logging
from telegram import Update

load_dotenv() 

token = os.environ.get("API_KEY")
# Función para manejar el comando "/start"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="¡Let's go!")

# Función para manejar el comando "/hello"
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# Configurar el bot
def main():
    # Configurar el registro de errores
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.ERROR)
    
    # Reemplaza 'TOKEN' con tu token de Telegram
    application = Application.builder().token(token).build()
    
    # Manejador para el comando "/start"
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('hello', hello))

    # Iniciar el bot
    application.run_polling()

if __name__ == '__main__':
    main()
#update proporciona información sobre la actualización recibida, mientras que context proporciona métodos y referencias para interactuar con la API de Telegram.