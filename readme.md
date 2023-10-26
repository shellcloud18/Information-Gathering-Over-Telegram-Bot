# Telegram Machine Info Bot

The Telegram Machine Info Bot is a Python script that connects to a Telegram bot and retrieves machine information when the `/getinfo` command is received. It fetches the folder name, file system information, and system information (such as operating system details and processor information) and sends them as a reply to the user through the Telegram bot.

## Prerequisites

- Python 3.6 or above
- `telebot` library (`pip install pyTelegramBotAPI`)

## Setup

1. Clone the repository or download the script file (`machine_info_bot.py`) to your computer.

2. Install the required dependencies by running the following command:
3. Obtain a Telegram bot token by following these steps:
- Create a new bot on Telegram by talking to the BotFather bot.
- Copy the bot token provided by the BotFather.

4. Open the `machine_info_bot.py` script in a text editor.

5. Replace `'YOUR_BOT_TOKEN'` with the bot token obtained in the previous step.

## Usage

1. Start the script by running the following command:
```
python machine_info_bot.py
