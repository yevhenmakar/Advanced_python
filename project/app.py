import telebot
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from flask import Flask, request, abort
import config
import keyboards
from models import models
from keyboards import ReplyKB

bot = telebot.TeleBot(config.TOKEN)
app = Flask(__name__)


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return ''


@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        abort(403)


@bot.message_handler(commands=['start'])
def start(message):
    # greetings_str = models.Texts(title='Greetings').get().body
    greeting_str = 'Hi'

    keyboard = ReplyKB().generate_kb(*keyboards.beginning_kb.values())
    bot.send_message(message.chat.id, greeting_str, reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == keyboards.beginning_kb['products'])
def show_categories(message):
    """
    :param message:
    :return: listed root categories
    """
    kb = keyboards.InlineKB(key='root', lookup_field='id', named_arg='category')
    bot.send_message(message.chat.id, "Choose category", reply_markup=kb.generate_kb())


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'category')
def show_products_or_sub_category(call):
    """
    :param call:
    :return: listed subcategories || listed products
    """
    obj_id = call.data.split('_')[1]
    category = models.Category.objects(id=obj_id).get()

    if category.is_parent:
        kb = keyboards.InlineKB(iterable=category.subcategory, lookup_field='id', named_arg='category')

        kb.generate_kb()
        kb.add(InlineKeyboardButton(text=f'back', callback_data=f'back_{category.id}'))

        bot.edit_message_text(text=category.title, chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              reply_markup=kb)
    # bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=kb.generate_kb())

    else:
        print("NON PARENT")


@bot.callback_query_handler(func=lambda call: call.data.split('_')[0] == 'back')
def go_back(call):
    obj_id = call.data.split('_')[1]
    category = models.Category.objects(id=obj_id).get()

    if category.is_root:
        kb = keyboards.InlineKB(key='root', lookup_field='id', named_arg='category', )
        kb.generate_kb()

    else:
        kb = keyboards.InlineKB(iterable=category.parent.subcategory, lookup_field='id', named_arg='category', )
        kb.generate_kb()
        kb.add(InlineKeyboardButton(text=f'<<{category.parent.title}', callback_data=f'back_{category.parent.id}'))

    text = 'Categories' if not category.parent else category.parent.title
    bot.edit_message_text(text=text, chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          reply_markup=kb)


if __name__ == '__main__':
    import time

    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(config.webhook_url,
                    certificate=open('webhook_cert.pem', 'r'))

    app.run(debug=True)
