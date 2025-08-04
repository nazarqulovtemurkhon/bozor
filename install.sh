#!/bin/bash

# WiFi Scanner Installation Script for Termux
# Author: Assistant

echo "🔧 WiFi Scanner o'rnatish boshlandi..."
echo "=================================="

# Check if we're in Termux
if [ ! -d "/data/data/com.termux" ]; then
    echo "❌ Bu dastur faqat Termux da ishlaydi!"
    exit 1
fi

# Update package list
echo "📦 Paketlar ro'yxatini yangilash..."
pkg update -y

# Install required packages
echo "📦 Kerakli dasturlarni o'rnatish..."
pkg install -y python termux-api

# Install Python packages
echo "🐍 Python kutubxonalarini o'rnatish..."
pip install requests

# Make scripts executable
echo "🔧 Dasturlarni ishga tushirish huquqini berish..."
chmod +x wifi_scanner.py
chmod +x wifi_cracker.py

# Create wordlist directory
echo "📝 Wordlist papkasini yaratish..."
mkdir -p /data/data/com.termux/files/usr/share/wordlists

# Download rockyou.txt if not exists
if [ ! -f "/data/data/com.termux/files/usr/share/wordlists/rockyou.txt" ]; then
    echo "📥 Rockyou wordlist yuklab olinmoqda..."
    wget -O /data/data/com.termux/files/usr/share/wordlists/rockyou.txt.gz https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt.gz
    gunzip /data/data/com.termux/files/usr/share/wordlists/rockyou.txt.gz
fi

echo ""
echo "✅ O'rnatish tugallandi!"
echo ""
echo "🎯 Foydalanish:"
echo "   python wifi_scanner.py    - Oddiy skaner (root talab qilmaydi)"
echo "   python wifi_cracker.py    - Kuchli cracker (root talab qiladi)"
echo ""
echo "📖 Batafsil ma'lumot uchun README.md faylini o'qing"
echo ""
echo "⚠️  Eslatma: Bu dastur faqat o'zingizning tarmoqlaringizni test qilish uchun!"