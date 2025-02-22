# Telegram Bot Project

This project is a Telegram bot built using the `aiogram` library. The bot can perform various tasks such as registering users, responding to commands, and handling different types of messages.

## Features

- Start the bot with a welcome message and a list of commands.
- Respond to specific text messages with predefined replies.
- Handle user registration through a series of questions.
- Provide a catalog of goods with inline keyboard buttons.
- Allow users to cancel the registration process at any time.

## Requirements

- Python 3.7+
- `aiogram` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/telegram-bot.git
    cd telegram-bot
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set your Telegram bot token in the main.py file:
    ```python
    bot = Bot(token='YOUR_TELEGRAM_BOT_TOKEN')
    ```

## Usage

1. Run the bot:
    ```sh
    python main.py
    ```

2. Interact with the bot on Telegram using the following commands:
    - `/start` - Start the bot and get a welcome message.
    - `/fart` - Make the bot send a fart emoji.
    - `/Register` - Start the user registration process.
    - `hi` - Greet the bot.
    - `fire` - Send a fire emoji.
    - `fuck you` - Swear at the bot.
    - `Catalog` - Get the catalog of goods.

3. During the registration process, you can cancel at any time by clicking the "Cancel" button.

## File Structure

- handlers.py: Contains the main logic for handling messages and commands.
- keyboard.py: Defines the keyboards used in the bot.
- main.py: Entry point for running the bot.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.