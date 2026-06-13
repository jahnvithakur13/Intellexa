import sqlite3
from datetime import datetime

conn = sqlite3.connect("chat_history.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_input TEXT,
    bot_response TEXT,
    timestamp TEXT
)
""")
conn.commit()

def save_chat(user, bot):
    cursor.execute(
        "INSERT INTO chats (user_input, bot_response, timestamp) VALUES (?, ?, ?)",
        (user, bot, str(datetime.now()))
    )
    conn.commit()

def get_chats():
    cursor.execute("SELECT user_input, bot_response FROM chats ORDER BY id ASC")
    return cursor.fetchall()

def delete_chats():
    cursor.execute("DELETE FROM chats")
    conn.commit()