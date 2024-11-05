import sqlite3
from datetime import datetime
from platform import version

bot = sqlite3.connect("users.db")
sql = bot.cursor()

sql.execute("CREATE TABLE IF NOT EXISTS users(user_id, reg_date DATETIME, version TEXT);")
bot.commit()
def add_user(user_id, version):
    bot = sqlite3.connect("users.db")
    sql = bot.cursor()
    sql.execute("INSERT INTO users (user_id, reg_date, version) VALUES (?,?,?)", (user_id, datetime.now(), version))
    bot.commit()
def check_user(user_id):
    bot = sqlite3.connect("users.db")
    sql = bot.cursor()
    check = sql.execute("SELECT * FROM users WHERE user_id=?", (user_id, )).fetchone()
    if check:
        return True
    elif not check:
        return False
def for_gpt(user_id):
    bot = sqlite3.connect("users.db")
    sql = bot.cursor()
    gpt_ver = sql.execute("SELECT version FROM users WHERE user_id=?", (user_id, )).fetchone()
    return gpt_ver
def change_verson(user_id, ver):
    bot = sqlite3.connect("users.db")
    sql = bot.cursor()
    sql.execute("UPDATE users SET version=? WHERE user_id=?", (ver, user_id))
    bot.commit()
def all_users():
    bot = sqlite3.connect("users.db")
    sql = bot.cursor()
    all_users = sql.execute("SELECT user_id FROM users").fetchall()
    users = [row[0] for row in all_users]
    bot.close()
    return users
