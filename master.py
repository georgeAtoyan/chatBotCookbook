import sqlite3
import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN


connect = sqlite3.connect('cookbook.db')
cursor = connect.cursor()
loop = asyncio.new_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)


# Group of Commands display the list of the dishes sorted by specified category
def show_dish_names(category):
    connect = sqlite3.connect('cookbook.db')
    cursor = connect.cursor()
    cursor.execute("SELECT name FROM recipe WHERE category = ?", (category,)) 
    items = cursor.fetchall()
    dish_names = [item[0] for item in items]
    return dish_names

def show_bakery_dishes():
    return show_dish_names('Выпечка')

def show_dessert_dishes():
    return show_dish_names('Десерты')

def show_hot_app_dishes():
    return show_dish_names('Горячие закуски')

def show_cold_app_dishes():
    return show_dish_names('Холодные закуски')

def show_salad_dishes():
    return show_dish_names('Салаты')

def show_soup_dishes():
    return show_dish_names('Супы')



