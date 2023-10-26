import platform
import subprocess
import telebot

# Telegram bot token
BOT_TOKEN = 'YOUR_BOT_TOKEN'

# Create an instance of the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Command handler for the /getinfo command
@bot.message_handler(commands=['getinfo'])
def handle_getinfo_command(message):
    machine_info = get_machine_info()
    bot.reply_to(message, machine_info)

# Retrieve machine information
def get_machine_info():
    # Get folder name
    folder_name = subprocess.check_output('echo %cd%', shell=True).decode().strip()

    # Get file system information
    fs_info = subprocess.check_output('fsutil fsinfo drives', shell=True).decode().strip()

    # Get system information
    system_info = platform.uname()

    # Construct the machine information string
    machine_info = f"Folder Name: {folder_name}\n\n" \
                   f"File System Information:\n{fs_info}\n\n" \
                   f"System Information:\n" \
                   f"  - System: {system_info.system}\n" \
                   f"  - Node Name: {system_info.node}\n" \
                   f"  - Release: {system_info.release}\n" \
                   f"  - Version: {system_info.version}\n" \
                   f"  - Machine: {system_info.machine}\n" \
                   f"  - Processor: {system_info.processor}"

    return machine_info

# Start the bot
bot.polling()
