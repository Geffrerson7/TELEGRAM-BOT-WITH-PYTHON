from telegram.ext import CommandHandler, Application, ContextTypes
import os
from dotenv import load_dotenv
import logging
from telegram import Update
import requests
from bs4 import BeautifulSoup

load_dotenv()

token = os.environ.get("API_KEY")

# Función para manejar el comando "/start"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="¡Hola!")

# Función para manejar el comando "/hello"
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# Función para realizar el scraping y enviar los enlaces al bot
async def scrape_pokemon(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    url = 'https://pokemon.gameinfo.io/es'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    pokemon_list = soup.find('div', class_='pokemon-list').find_all('div', class_='gen')[:10]

    links = []
    for pokemon in pokemon_list:
        pokemon_id = pokemon.find('div', class_='id').text.strip()
        pokemon_name = pokemon.find('h2').text.strip().lower()
        link = f'https://pokemon.gameinfo.io/es/pokemon/{pokemon_id}-{pokemon_name}'
        links.append(link)

    links_text = '\n'.join(links)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=links_text)

# Configurar el bot
def main():
    # Configurar el registro de errores
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.ERROR)

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('hello', hello))
    application.add_handler(CommandHandler('scrape', scrape_pokemon))  # Manejador para el comando "/scrape"

    application.run_polling()

if __name__ == '__main__':
    main()
