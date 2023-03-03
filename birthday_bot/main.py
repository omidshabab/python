import telegram.ext
import sqlite3

TOKEN = open("TOKEN.txt", "r").read()

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

def cancel():
    pass