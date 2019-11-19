from models import models
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


beginning_kb = {
    'news': 'Последние новости',
    'products': 'Продукты',
    'sales': 'Продукты со скидкой',
    'about': 'Информация о магазине',
}


class ReplyKB(ReplyKeyboardMarkup):
    def __init__(self, one_time_keyboard=False, resize_keyboard=True, row_width=3):
        super().__init__(one_time_keyboard=one_time_keyboard,
                         resize_keyboard=resize_keyboard,
                         row_width=row_width)

    def generate_kb(self, *args):
        """
        :param args: Buttons names
        :return: new kb
        """
        buttons = [KeyboardButton(x) for x in args]
        self.add(*buttons)
        return self


class InlineKB(InlineKeyboardMarkup):

    def __init__(self, iterable, named_arg, lookup_field='id', title_field='title', row_width=3):
        super().__init__(row_width=row_width)
        self._iterable = iterable
        self._named_arg = named_arg
        self._lookup_field = lookup_field
        self._title_field = title_field

    def generate_kb(self):
        buttons = []

        for i in self._iterable:
            buttons.append(InlineKeyboardButton(
                text=str(getattr(i, self._title_field)),
                callback_data=f'{self._named_arg}_' + str(getattr(i, self._lookup_field))
            ))

        self.add(*buttons)
        return self