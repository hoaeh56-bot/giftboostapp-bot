import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.telegram import TelegramAPIServer
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import CommandStart
import config

logging.basicConfig(level=logging.INFO)

session = AiohttpSession(api=TelegramAPIServer.from_base(config.API_SERVER))
bot = Bot(token=config.BOT_TOKEN, session=session)
dp = Dispatcher()

# --- СТАРТ ---
@dp.message(CommandStart())
async def cmd_start(message: Message):
    # Ссылка на твой проект Vercel
    WEB_APP_URL = "https://misu-portal.vercel.app/"
    
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Начать играть", web_app=WebAppInfo(url=WEB_APP_URL))]
    ])
    
    await message.answer(
        "Добро пожаловать в <b>Gift Boost</b>! 🚀\n"
        "Нажми на кнопку ниже, чтобы начать.",
        reply_markup=kb,
        parse_mode="HTML"
    )

async def main():
    logging.info("🚀 Бот Gift Boost запущен.")
    try:
        await bot.delete_webhook(drop_pending_updates=True)
    except Exception:
        pass
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())