import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
import os

# Токен берётся из переменной окружения (безопасно)
TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🔥 Это место для твоих болей, обид и всего лишнего.\n\n"
        "Напиши что угодно — и это исчезнет навсегда.\n"
        "Никто не увидит. Никакой истории."
    )


@dp.message(F.text)
async def burn_message(message: Message):
    # Удаляем сообщение пользователя
    try:
        await message.delete()
    except Exception:
        pass  # если нет прав — просто пропускаем

    # Отправляем подтверждение и тут же удаляем его через 3 секунды
    confirm = await message.answer("🔥 сожжено")
    await asyncio.sleep(3)
    try:
        await confirm.delete()
    except Exception:
        pass


@dp.message()
async def burn_any(message: Message):
    # Удаляем любые другие типы сообщений (фото, голос и т.д.)
    try:
        await message.delete()
    except Exception:
        pass
    confirm = await message.answer("🔥 сожжено")
    await asyncio.sleep(3)
    try:
        await confirm.delete()
    except Exception:
        pass


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
