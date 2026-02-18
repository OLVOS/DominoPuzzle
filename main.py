import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

# ВСТАВЬ СВОЙ НОВЫЙ ТОКЕН (тот старый заблокируй в BotFather!)
TOKEN = 'ТВОЙ_ТОКЕН_ЗДЕСЬ'

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    # Создаем клавиатуру с кнопкой Web App
    builder = InlineKeyboardBuilder()
    # ВАЖНО: url должен вести на работающий сайт (https).
    # Для теста можно использовать https://google.com, чтобы проверить, что кнопка жмется
    builder.row(types.InlineKeyboardButton(
        text="Открыть Pips MVP",
        web_app=types.WebAppInfo(url="https://твоя-ссылка.github.io/index.html")
    ))

    await message.answer(
        "Привет! Нажми на кнопку ниже, чтобы запустить игру:",
        reply_markup=builder.as_markup()
    )

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())