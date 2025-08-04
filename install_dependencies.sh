#!/bin/bash
# WiFi Password Finder uchun kerakli dasturlarni o'rnatish

echo "🔧 WiFi Password Finder uchun kerakli dasturlar o'rnatilmoqda..."
echo "=================================================="

# Termux paketlarini yangilash
echo "📦 Paketlar yangilanmoqda..."
pkg update -y
pkg upgrade -y

# Kerakli dasturlarni o'rnatish
echo "🔧 Kerakli dasturlar o'rnatilmoqda..."

# Python va kerakli kutubxonalar
pkg install python -y
pkg install python-pip -y

# WiFi skaner va parol topish dasturlari
pkg install aircrack-ng -y
pkg install wireless-tools -y
pkg install net-tools -y

# Qo'shimcha foydali dasturlar
pkg install nmap -y
pkg install macchanger -y

# Python kutubxonalarini o'rnatish
echo "📚 Python kutubxonalari o'rnatilmoqda..."
pip install colorama
pip install requests
pip install psutil

echo ""
echo "✅ Barcha dasturlar muvaffaqiyatli o'rnatildi!"
echo ""
echo "🚀 Dasturni ishga tushirish uchun:"
echo "   python wifi_password_finder.py"
echo ""
echo "⚠️  Eslatma: Bu dastur faqat o'zingizning tarmoqlaringizda ishlatilishi kerak!"
echo "   Boshqalarning WiFi tarmoqlariga ruxsatsiz kirish qonunga zid!"