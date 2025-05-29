"""Файл с хендлерами бота."""

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import asyncio

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка команды /start."""
    keyboard = [
        [InlineKeyboardButton("🎲 Рандомный факт", callback_data="random_fact")],
        [InlineKeyboardButton("🤖 ChatGPT", callback_data="gpt_interface")],
        [InlineKeyboardButton("👥 Диалог с личностью (скоро)", callback_data="talk_coming_soon")],
        [InlineKeyboardButton("🧠 Квиз (скоро)", callback_data="quiz_coming_soon")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_text = (
        "🎉 <b>Добро пожаловать в ChatGPT бота!</b>\n\n"
        "🚀 <b>Доступные функции:</b>\n"
        "• Рандомный факт - получи интересный факт\n"
        "• ChatGPT - общение с ИИ\n"
        "• Диалог с личностью - говори с известными людьми (в разработке)\n"
        "• Квиз - проверь свои знания (в разработке)\n\n"
        "Выберите функцию из меню ниже:"
    )

    await update.message.reply_text(welcome_text, parse_mode='HTML', reply_markup=reply_markup)


async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка нажатий кнопок главного меню"""
    query = update.callback_query
    await query.answer()

    if query.data == "random_fact":
        pass
    elif query.data == "gpt_interface":
        pass

    elif query.data in ["talk_coming_soon", "quiz_coming_soon"]:
        await query.edit_message_text(
            "🚧 <b>Функция в разработке!</b>\n\n"
            "Эта функция будет добавлена на следующих уроках.\n"
            "Пока что попробуйте 'Рандомный факт'!",
            parse_mode='HTML'
        )

        await asyncio.sleep(3)
        await start_menu_again(query)


async def start_menu_again(query):
    """Возврат в главное меню"""
    keyboard = [
        [InlineKeyboardButton("🎲 Рандомный факт", callback_data="random_fact")],
        [InlineKeyboardButton("🤖 ChatGPT", callback_data="gpt_interface")],
        [InlineKeyboardButton("👥 Диалог с личностью (скоро)", callback_data="talk_coming_soon")],
        [InlineKeyboardButton("🧠 Квиз (скоро)", callback_data="quiz_coming_soon")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        "🎉 <b>Добро пожаловать в ChatGPT бота!</b>\n\n"
        "Выберите одну из доступных функций:",
        parse_mode='HTML',
        reply_markup=reply_markup
    )
