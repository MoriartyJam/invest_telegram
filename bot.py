import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token='7181098500:AAEEjoy9gIdj5rLU98zB-bgK5VDELwKEIog', parse_mode="HTML")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Subscribe")],
        [types.KeyboardButton(text="Support")],
        [types.KeyboardButton(text="FAQ")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Please choice right answer"
    )
    await message.answer("How can I help you?", reply_markup=keyboard)

@dp.message(F.text == "Support")
async def with_puree(message: types.Message):
    await message.reply('<a href="https://www.google.com/">Support</a>')

@dp.message(F.text == "FAQ")
async def   without_puree(message: types.Message):

    await message.answer(
        '<b>Возможно ли купить подписку на месяц?</b>\n' \
        '<pre>    Подписки на месяц в DOUBLETOP SQUAD больше нет (только если вы ранее не покупали подписку и не продлевали ее непрерывно\n</pre>'
        '<b>Я оплатил, а бот написал что платеж был просрочен, что делать?</b>\n' \
        '<pre>    Как только вы нажимаете кнопку "перейти к оплате" - формируется ссылка и адрес для оплаты только на 15 МИНУТ (остаток времени можно проверять по ссылке). Если вы оплатили после 15 минут / переплатили / недоплатили - в автоматическом режиме формируется письмо вам на почту с информацией для рефанда - соответственно доступ к подписке вы не получите.</pre>\n'
        '<b>Почему клавиатура в боте на работает?\n</b>' \
        '<pre>    Скорее всего, у вас не обновилась клавиатура. Перезапустите бота используя команду /start</pre>\n' \
        '<b>При подключение к дискорд пишет "Что-то пошло не так". Что делать?\n</b>' \
        '<pre>    Попробуйте перезапусить бота используя команду /start. После этого - попробуйте подключить дискорд еще раз.</pre>\n' \
        'Если трудности остались - напишите в суппорт.\n' \
        )

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())