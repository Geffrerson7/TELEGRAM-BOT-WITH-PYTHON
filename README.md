# TELEGRAM-BOT-WITH-PYTHON

Telegram bot to search for web links with information about Pokemon by Pokemon ID.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`: TELEGRAM BOT TOKEN

## Local installation

Clone the project

```bash
  git clone https://github.com/Geffrerson7/TELEGRAM-BOT-WITH-PYTHON.git
```

Go to the project directory

```bash
  cd TELEGRAM-BOT-WITH-PYTHON
```

Create virtual enviroment

```bash
$ virtualenv venv
```

Translate to English: Activate the virtual environment.

```bash
$ venv\Scripts\activate
```

Install dependencies

```bash
$(venv) pip install -r requirements.txt
```

Run project

```bash
$(venv)  py telegram-bot.py
```

## Local installation with Dcoker

Clone the project

```bash
  git clone https://github.com/Geffrerson7/TELEGRAM-BOT-WITH-PYTHON.git
```

Go to the project directory

```bash
  cd TELEGRAM-BOT-WITH-PYTHON
```

Create Docker image

```bash
$ docker build -t image_name .
```

Run Docker container

```bash
$ docker run image_name
```

## Start the Telegram bot's start menu

Send the following message to the bot:

```bash
  /start
```