from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Command
from aiogram import executor
import sqlite3


from keyboard import *
from master import bot, dp
from master import show_bakery_dishes, show_dessert_dishes, show_hot_app_dishes, show_cold_app_dishes, show_salad_dishes, show_soup_dishes


connect = sqlite3.connect('cookbook.db')
cursor = connect.cursor()

# Handler activates Inroduction
@dp.message_handler(Command('start'))
async def display(message: Message):
    await message.answer(text='Добро пожаловать в чат-бот!\n')
    await message.answer(text='Для запуска меню введите команду /пуск\n')

# Handler activates Command /пуск and displays Главное меню
@dp.message_handler(Command('пуск'))
async def display(message: Message):
    await message.answer(text='Главное меню:',reply_markup=parent_keyboard)

# Handler activates button Обычный поиск
@dp.callback_query_handler(lambda c: c.data == 'button_1')
async def process_button1(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id, "Введите название блюда: ")
    dp.register_message_handler(process_input1, lambda message: message.from_user.id == callback_query.from_user.id)

async def process_input1(message: Message):
    input_text = message.text
    cursor.execute("SELECT * FROM recipe WHERE name LIKE '{}%'".format(input_text))
    items = cursor.fetchall()
    response_text = ""
    if items:
        response_text = "По вашему запросу найдено: \n\n"
        for recipe in items:
            response_text += recipe[0] + "\n"
            cursor.execute("SELECT ingredients, recipe FROM recipe WHERE name = ?", (recipe[0],))
            result = cursor.fetchone()
            response_text += f"Ингредиенты:\n{result[0]}\n\n"
            response_text += f"Рецепт:\n{result[1]}\n"
        await bot.send_message(chat_id=message.chat.id, text=response_text, reply_markup=extra_keyboard2) 
    else:
        await message.answer(text="Совпадений не найдено")

# Handler activates button Поиск по категориям
@dp.callback_query_handler(lambda c: c.data == 'button_2')
async def process_button2(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id, text = "Пожалуйста выберете категорию:", reply_markup=child_keyboard)
 
    
# Set of handlers for child_buttons

@dp.callback_query_handler(lambda c: c.data in ['child_button_1','child_button_2', 'child_button_3', 'child_button_4', 'child_button_5', 'child_button_6'])
async def process_callback_query(callback_query: CallbackQuery):
    if callback_query.data == 'child_button_1':
        dish_names = show_bakery_dishes()
    elif callback_query.data == 'child_button_2':
        dish_names = show_dessert_dishes()
    elif callback_query.data == 'child_button_3':
        dish_names = show_hot_app_dishes()
    elif callback_query.data == 'child_button_4':
        dish_names = show_cold_app_dishes()
    elif callback_query.data == 'child_button_5':
        dish_names = show_salad_dishes()
    elif callback_query.data == 'child_button_6':
        dish_names = show_soup_dishes()

    for dish_name in dish_names:
        message = f"{dish_name}\n\n"
        connect = sqlite3.connect('cookbook.db')
        cursor = connect.cursor()
        cursor.execute("SELECT ingredients, recipe FROM recipe WHERE name = ?", (dish_name,))
        result = cursor.fetchone()
        message += f"Ингредиенты:\n{result[0]}\n\n"
        message += f"Рецепт: {result[1]}\n"
        await bot.send_message(callback_query.from_user.id, message, reply_markup=extra_keyboard)

# Handlers activate button Возврат в главное меню
@dp.callback_query_handler(lambda c: c.data == 'child_button_7')
async def process_button_return(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id ,text='Возврат в главное меню:', reply_markup=parent_keyboard)

@dp.callback_query_handler(lambda c: c.data == 'back_category_keyboard')
async def process_return(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id ,text='Возврат в Категорию:', reply_markup=child_keyboard)

@dp.callback_query_handler(lambda c: c.data == 'back_menu_keyboard')
async def process_return(callback_query: CallbackQuery):
    await bot.send_message(callback_query.from_user.id ,text='Возврат в главное меню:', reply_markup=parent_keyboard)

if __name__ == '__main__':
    executor.start_polling(dp)
    
connect.commit()
connect.close()
