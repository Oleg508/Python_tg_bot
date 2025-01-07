from aiogram import  F, types,Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command,or_f
from aiogram.utils.formatting import as_list,as_marked_section,Bold

from filters.chat_types import ChatTypeFilter
from kbds import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(text="Привет я виртуальный помощник",reply_markup=reply.start_kb3.as_markup(resize_keyboard = True,input_field_placeholder = 'Что вас интересует ?'))


@user_private_router.message(or_f(Command('menu') ,(F.text.lower() == "меню")))
async def menu_cmd(message: types.Message):
    await message.answer("Вот меню:",reply_markup=reply.del_kbd)

@user_private_router.message(F.text.lower() == 'о магазине')
@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer("О магазине:")

@user_private_router.message(F.text.lower() == 'варианты оплаты')
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message):
    text = as_marked_section(
        Bold('Варианты оплаты:'),
        'Картой в боте',
        'При получении картой/наличными',
        'В заведении',
        marker='✅'
    )

    await message.answer(text.as_html())    

@user_private_router.message((F.text.lower().contains("доставк")) | (F.text.lower() == 'варианты доставки'))
@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message):
    text = as_list(
        as_marked_section(
            Bold("Варинты доставки/заказа"),
            'Курьер',
            'Самовывоз',
            'Покушаю у вас',
            marker = '✅'
        ),
        as_marked_section(
            Bold('Нельзя'),
            'Почта',
            'Голуби',
            marker= '⛔️'
        ),
        sep='\n................................\n'
    )
    await message.answer(text.as_html())     

@user_private_router.message(F.contact)
async def get_contact(message:types.Message):
    await message.answer(f"номер получен")
    await message.answer(str(message.contact))

@user_private_router.message(F.location)
async def get_contact(message:types.Message):
    await message.answer(f"локация получена")
    await message.answer(str(message.locationt))


@user_private_router.message(F.photo)
async def shipping_cmd(message: types.Message):
    await message.answer("Классная фоточка!")   
