from pyrogram import Client
from pyrogram import filters
from pyrogram import types
import sqlite3
import time
import random
import asyncio
app = Client('my_accounts')

my_id = 1307813926
mess_id = 3112
voise = 'AwACAgIAAxkBAAIMJ2B5sns30cnQioGIRflM-BRBSzj5AAKZDgACjEPIS2wHWeY5UTCaHgQ'


@app.on_message(filters.command('b'))
async def echo (client,message):
    if message.from_user.id == my_id:
        pass


@app.on_message()
async def sdasd (client,message):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(""" CREATE TABLE IF NOT EXISTS user_time (
            id,
            status_ref
            ) """)
    db.commit()

    sql.execute(f"SELECT id FROM user_time WHERE id ='{message.chat.id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user_time VALUES (?,?)", (message.chat.id, 1))
        db.commit()
        await asyncio.sleep(120)
        await app.send_voice(chat_id=message.chat.id, voice=voise)
        await asyncio.sleep(15)
        await app.copy_message(chat_id=message.chat.id, from_chat_id=my_id,message_id=mess_id)
    else:
        print('Зарегистрирован')

app.run()