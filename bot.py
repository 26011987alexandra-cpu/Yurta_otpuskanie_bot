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
        "Тебя приветствует особый уголок Юрты Уюта, где может быть высказано и прозвучать то, что хранилось годами. "
        "Это место для твоих болей, обид, безжизненного и того, чему пришло время быть высказанным и уйти в переработку во благо живого.\n\n"
        "Напиши — и это исчезнет навсегда.\n"
        "Никто не увидит. Конфиденциально и мягко."
    )


@dp.message(F.text)
async def burn_message(message: Message):
    # Удаляем сообщение пользователя
    try:
        await message.delete()
    except Exception:
        pass  # если нет прав — просто пропускаем

    # Отправляем подтверждение и тут же удаляем его через 3 секунды
    confirm = await message.answer("Обнимаю с Любовью🤍")
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
    confirm = await message.answer("Обнимаю с Любовью🤍")
    await asyncio.sleep(3)
    try:
        await confirm.delete()
    except Exception:
        pass


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
