# Cryptocurrency Telegram Bot

This repository contains a Telegram bot designed to manage and track cryptocurrency balances for users. The bot fetches real-time cryptocurrency prices and allows users to update and view their wallet balances through simple commands.

---

## Features

- Fetch live cryptocurrency prices using Binance API (via `ccxt`).
- Manage user balances for cryptocurrencies: BTC, ETH, SOL, and TON.
- View total wallet balance in USD.
- Store user data securely in an SQLite database.
- Interactive Telegram bot commands for ease of use.

---

## Installation

### Requirements

- Python 3.9+
- Telegram bot token (can be obtained via [BotFather](https://core.telegram.org/bots#botfather)).
- Dependencies: Install from `requirements.txt`.

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/py-dima/Crypto-Balance-Bot.git
    cd crypto-telegram-bot
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure environment variables:
    Create a `.env` file in the root directory:
    ```env
    BOT_TOKEN=your_telegram_bot_token
    ```

4. Set up the database:
    Ensure the `base.db` file is in the root directory with the appropriate schema:
    - Table: `main`
    - Columns: `id` (user ID), `username`, `btc`, `eth`, `sol`, `ton`.

5. Run the bot:
    ```bash
    python main.py
    ```

---

## Usage

- Start the bot with `/start` to initialize your profile.
- Update your wallet balance:
  - `/btc <amount>`: Update BTC balance.
  - `/eth <amount>`: Update ETH balance.
  - `/sol <amount>`: Update SOL balance.
  - `/ton <amount>`: Update TON balance.
- View your wallet balance with `/balance`.

---

## Project Structure

- `.env`: Environment variables.
- `1.py`: Fetches live cryptocurrency prices for specified symbols.
- `docs.py`: Provides a reusable function to fetch prices for a single symbol.
- `main.py`: Core bot logic, including database and command handling.
- `base.db`: SQLite database for storing user balances.

---

## Contribution

Feel free to contribute by forking this repository, making changes, and submitting a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

# Телеграм-бот для роботи з криптовалютами

Цей репозиторій містить Телеграм-бота для управління та відстеження балансу криптовалют користувачів. Бот отримує актуальні ціни на криптовалюти та дозволяє користувачам оновлювати і переглядати баланси своїх гаманців через прості команди.

---

## Можливості

- Отримання актуальних цін криптовалют через Binance API (за допомогою `ccxt`).
- Управління балансами користувачів для криптовалют: BTC, ETH, SOL, TON.
- Перегляд загального балансу гаманця у USD.
- Безпечне зберігання даних користувачів у базі SQLite.
- Інтерактивні команди Телеграм-бота для зручного використання.

---

## Встановлення

### Вимоги

- Python 3.9+
- Токен Телеграм-бота (можна отримати через [BotFather](https://core.telegram.org/bots#botfather)).
- Залежності: встановіть із `requirements.txt`.

### Кроки

1. Клонуйте репозиторій:
    ```bash
    git clone https://github.com/py-dima/Crypto-Balance-Bot.git
    cd crypto-telegram-bot
    ```

2. Встановіть залежності:
    ```bash
    pip install -r requirements.txt
    ```

3. Налаштуйте змінні середовища:
    Створіть файл `.env` у кореневій директорії:
    ```env
    BOT_TOKEN=your_telegram_bot_token
    ```

4. Налаштуйте базу даних:
    Переконайтесь, що файл `base.db` знаходиться у кореневій директорії та має відповідну структуру:
    - Таблиця: `main`
    - Колонки: `id` (ID користувача), `username`, `btc`, `eth`, `sol`, `ton`.

5. Запустіть бота:
    ```bash
    python main.py
    ```

---

## Використання

- Запустіть бота командою `/start`, щоб ініціалізувати ваш профіль.
- Оновлюйте баланс гаманця:
  - `/btc <сума>`: Оновлення балансу BTC.
  - `/eth <сума>`: Оновлення балансу ETH.
  - `/sol <сума>`: Оновлення балансу SOL.
  - `/ton <сума>`: Оновлення балансу TON.
- Перегляньте баланс гаманця командою `/balance`.

---

## Структура проекту

- `.env`: Змінні середовища.
- `1.py`: Отримання актуальних цін криптовалют для заданих символів.
- `docs.py`: Функція для отримання ціни одного символу.
- `main.py`: Основна логіка бота, включаючи базу даних та обробку команд.
- `base.db`: База даних SQLite для збереження балансів користувачів.

---

## Внесок

Ви можете зробити свій внесок, форкнувши цей репозиторій, внісши зміни та створивши pull request.

---

## Ліцензія

Цей проект ліцензовано за ліцензією MIT. Деталі дивіться у файлі LICENSE.

