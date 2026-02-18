import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Твой токен от @BotFather
TOKEN = '8300783229:AAFOhluOfALJCI_ujvYks1gXLH4RfOmM7lk'

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    builder = InlineKeyboardBuilder()

    # Твоя рабочая ссылка
    game_url = "https://olvos.github.io/DominoPuzzle/"

    builder.row(types.InlineKeyboardButton(
        text="🧩 Играть в Pips",
        web_app=types.WebAppInfo(url=game_url)
    ))

    await message.answer(
        "Добро пожаловать в Pips! Нажми кнопку, чтобы открыть игру:",
        reply_markup=builder.as_markup()
    )


async def main():
    print("Бот запущен и ждет игроков...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())