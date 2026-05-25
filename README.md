# 🚀 Free VPN Telegram Bot

ربات تلگرامی رایگان ارائه‌دهنده کانفیگ VPN

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/aiogram-3.x-2C8EBB" alt="aiogram">
  <img src="https://img.shields.io/badge/Telegram-Bot-229ED9?logo=telegram&logoColor=white" alt="Telegram Bot">
</div>

## ✨ ویژگی‌ها

- **ارائه کانفیگ رایگان** (VMess, VLESS, Trojan و ...)
- **پشتیبانی از چندین پروتکل**
- **سیستم مدیریت کاربران**
- **به‌روزرسانی خودکار کانفیگ‌ها**
- **کیبوردهای اینلاین و ریپلای**
- **ذخیره‌سازی اطلاعات در JSON**
- **قابلیت گسترش آسان**

## 📁 ساختار پروژه

```bash
free-vpn-tg-bot/
├── bot.py                 # فایل اصلی راه‌اندازی ربات
├── config.py              # تنظیمات و کانفیگ‌ها
├── keyboards.py           # مدیریت کیبوردهای ربات
├── handlers/
│   ├── __init__.py
│   └── user.py            # هندلرهای کاربر
├── data/
│   └── configs.json       # ذخیره کانفیگ‌های VPN
├── .env.example
├── requirements.txt
├── README.md
└── .gitignore
