import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from config import BOT_TOKEN, CHANNEL_ID, CHANNEL_USERNAME, ADMIN_ID
from keyboards import main_menu, config_types_menu
from handlers.user import check_subscription, send_config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    if not await check_subscription(bot, message.from_user.id, CHANNEL_ID):
        await message.answer(
            "❗ <b>برای استفاده از ربات باید اول در کانال عضو شوید:</b>",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
                InlineKeyboardButton("عضو شدن در کانال ✅", url=f"https://t.me/{CHANNEL_USERNAME}")
            ], [
                InlineKeyboardButton("✅ بررسی عضویت", callback_data="check_join")
            ]])
        )
        return

    await message.answer(
        f"👋 سلام <b>{message.from_user.first_name}</b>!\n\n"
        "به ربات کانفیگ رایگان خوش آمدید.\n"
        "از دکمه‌های زیر استفاده کنید:",
        reply_markup=main_menu()
    )

@dp.callback_query(F.data == "check_join")
async def check_join(callback: CallbackQuery):
    if await check_subscription(bot, callback.from_user.id, CHANNEL_ID):
        await callback.message.edit_text("✅ عضویت شما تأیید شد!\n\nاز منوی اصلی استفاده کنید:", reply_markup=main_menu())
    else:
        await callback.answer("❌ هنوز عضو کانال نشده‌اید!", show_alert=True)

@dp.callback_query(F.data == "get_free_config")
async def get_config(callback: CallbackQuery):
    await callback.message.edit_text("نوع کانفیگ مورد نظر را انتخاب کنید:", reply_markup=config_types_menu())

# هندلرهای بقیه را بعدا اضافه می‌کنیم
@dp.callback_query()
async def all_callbacks(callback: CallbackQuery):
    await callback.answer("این بخش هنوز در حال توسعه است...")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
