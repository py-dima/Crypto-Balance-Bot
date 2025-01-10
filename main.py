import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
import sqlite3
import ccxt

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(text = "Вітаю в моєму крипто-боті!")

    with sqlite3.connect('base.db') as db:
        cursor = db.cursor()
        cursor.execute(f"""SELECT id FROM main WHERE id = {message.from_user.id}""")
        users = cursor.fetchall()
        if not users:
            cursor.execute(f"""INSERT INTO main (id, username, btc, eth, sol, ton) VALUES({message.from_user.id}, '{message.from_user.username}', 0, 0, 0, 0) """)
            db.commit

# @dp.message(Command("btc"))
# async def cmd_start(message: types.Message):
#     total = message.text.split(" ")[1]
#     try:
#         with sqlite3.connect('base.db') as db:
#             cursor = db.cursor()
#             cursor.execute(f"""UPDATE main set btc = {total} WHERE id = {message.from_user.id} """)
#             db.commit

#         await message.answer(text = f"{total} BTC успішно зараховані на ваш баланс!")
#     except:
#         await message.answer(text = "Помилка в форматі повідомлення. Вкажіть число BTC без пробілів і ком. Або ціле число, або дробне але через крапку \n\nПриклад:\n <code>/btc 1</code> | <code>/btc 1.5</code>", parse_mode="HTML")

wallet = ("btc", "eth", "sol", "ton")

@dp.message(Command(commands=wallet))
async def cmd_start(message: types.Message, command: Command):
    cmd = command.command
    total = message.text.split(" ")[1]
    try:
        with sqlite3.connect('base.db') as db:
            cursor = db.cursor()
            cursor.execute(f"""UPDATE main set {cmd} = {total} WHERE id = {message.from_user.id} """)
            db.commit

        await message.answer(text = f"{total} {cmd.upper()} успішно зараховані на ваш баланс!")
    except:
        await message.answer(text = f"Помилка в форматі повідомлення. Вкажіть число {cmd.upper()} без пробілів і ком. Або ціле число, або дробне але через крапку \n\nПриклад:\n <code>/{cmd.upper()} 1</code> | <code>/{cmd.upper()} 1.5</code>", parse_mode="HTML")

@dp.message(Command("balance"))
async def cmd_start(message: types.Message):
    with sqlite3.connect('base.db') as db:
        cursor = db.cursor()
        cursor.execute(f"""SELECT btc, eth, sol, ton FROM main WHERE id = {message.from_user.id}""")
        total = cursor.fetchall()[0]

        exchange = ccxt.binance()

        symbols = ["BTC/USDT", "ETH/USDT", "SOL/USDT", "TON/USDT"]
        prices = [] # Пустий список, в якому будуть ціни
        for symbol in symbols:
            price = exchange.fetch_ticker(symbol)['last']
            prices.append(price)
        # btc_usdt = total[0] * prices[0]
        total_usdt = []
        for a, b in zip(total, prices):
            total_usdt.append(a * b)

        await message.answer(text= f"<b>Your wallet balance</b>\n\n BTC: {total[0]} (${int(total_usdt[0])})\n ETH: {total[1]} (${int(total_usdt[1])})\n SOL: {total[2]} (${int(total_usdt[2])})\n TON: {total[3]} (${int(total_usdt[3])})\n\n <b>Total:</b> ${sum(total_usdt)}", parse_mode="HTML" )

async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())