from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

parent_keyboard = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text='Обычный поиск', callback_data='button_1'),
            InlineKeyboardButton(text='Поиск по категориям', callback_data='button_2')
        ]
    ]
)

child_keyboard = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text='Выпечка', callback_data='child_button_1'),
            InlineKeyboardButton(text='Десерты', callback_data='child_button_2'),
        ],
        [
            InlineKeyboardButton(text='Горячие закуски', callback_data='child_button_3'),
            InlineKeyboardButton(text='Холодные закуски', callback_data='child_button_4'),
        ],
        [
            InlineKeyboardButton(text='Салаты', callback_data='child_button_5'),
            InlineKeyboardButton(text='Супы', callback_data='child_button_6')
        ],
        [
            InlineKeyboardButton(text='Возврат в главное меню', callback_data='child_button_7')
        ]
    ]
)

extra_keyboard = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text="Назад в Категорию", callback_data='back_category_keyboard'),
            InlineKeyboardButton(text="Назад в главное меню", callback_data='back_menu_keyboard')
        ]
    ]
)

extra_keyboard2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Возврат в главное меню", callback_data='back_menu_keyboard')
        ]
    ]
)
