from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("📥 دریافت کانفیگ رایگان", callback_data="get_free_config")],
        [InlineKeyboardButton("🔄 کانفیگ جدید", callback_data="new_config")],
        [InlineKeyboardButton("📚 راهنما و آموزش", callback_data="help")],
        [InlineKeyboardButton("🌐 کانال ما", url=f"https://t.me/{CHANNEL_USERNAME}")],
    ])

def config_types_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⚡ VLESS", callback_data="type_vless")],
        [InlineKeyboardButton("🔰 VMess", callback_data="type_vmess")],
        [InlineKeyboardButton("🛡️ Trojan", callback_data="type_trojan")],
        [InlineKeyboardButton("🔙 بازگشت به منو", callback_data="back_main")],
    ])
