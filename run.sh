#!/bin/bash
# WiFi Password Finder ishga tushirish skripti

echo "🔐 WiFi Password Finder - Termux uchun"
echo "======================================"

# Python mavjudligini tekshirish
if ! command -v python &> /dev/null; then
    echo "❌ Python o'rnatilmagan!"
    echo "📦 O'rnatish uchun: pkg install python"
    exit 1
fi

# Fayllar mavjudligini tekshirish
if [ ! -f "wifi_password_finder.py" ]; then
    echo "❌ wifi_password_finder.py fayli topilmadi!"
    exit 1
fi

# Root huquqlarini tekshirish
if [ "$(whoami)" != "root" ]; then
    echo "⚠️  Root huquqlari kerak emas, lekin ba'zi funksiyalar ishlamasligi mumkin"
    echo "💡 Root bo'lish uchun: su"
fi

# Dasturni ishga tushirish
echo "🚀 Dastur ishga tushirilmoqda..."
echo ""

# Oddiy versiyani ishga tushirish
python wifi_password_finder.py

echo ""
echo "✅ Dastur tugadi!"