import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = '8300783229:AAFOhluOfALJCI_ujvYks1gXLH4RfOmM7lk'  # ← твой токен

# URL к твоей GitHub Pages (сюда залей index.html)
GAME_URL = "https://olvos.github.io/DominoPuzzle/"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="🧩 Играть в Pips",
        web_app=types.WebAppInfo(url=GAME_URL)
    ))

    await message.answer(
        "🎲 *PIPS DAILY*\n\n"
        "Размести все костяшки домино на сетке так, чтобы выполнить условия каждой зоны:\n\n"
        "• Число → сумма пипсов в зоне равна числу\n"
        "• `=` → все пипсы в зоне одинаковые\n"
        "• `≠` → все пипсы в зоне разные\n"
        "• `>N` / `<N` → каждый пипс больше/меньше N\n\n"
        "Одно домино может перекрывать *две* зоны — каждая половинка выполняет правило своей зоны.",
        parse_mode="Markdown",
        reply_markup=builder.as_markup()
    )


async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())