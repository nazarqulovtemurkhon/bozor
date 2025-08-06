#!/bin/bash
# WiFi Password Cracker Setup Script for Termux

echo "🔓 WiFi Password Cracker - O'rnatish"
echo "====================================="

# Update package list
echo "📦 Paketlar ro'yxatini yangilash..."
pkg update -y

# Upgrade packages
echo "⬆️  Paketlarni yangilash..."
pkg upgrade -y

# Install required packages
echo "📥 Kerakli dasturlarni o'rnatish..."
pkg install -y python
pkg install -y aircrack-ng
pkg install -y wireless-tools
pkg install -y git

# Make the Python script executable
echo "🔧 Dasturni ishga tushirish uchun tayyorlash..."
chmod +x wifi_cracker.py

# Create wordlist directory
echo "📝 Wordlist papkasini yaratish..."
mkdir -p /data/data/com.termux/files/home/wordlists

echo ""
echo "✅ O'rnatish tugallandi!"
echo ""
echo "🚀 Dasturni ishga tushirish uchun:"
echo "   python wifi_cracker.py"
echo ""
echo "📋 Yoki:"
echo "   ./wifi_cracker.py"
echo ""
echo "⚠️  Eslatma: Bu dastur faqat o'zingizning tarmoqlaringizda ishlatilishi kerak!"
echo "   Boshqalarning tarmoqlariga ruxsatsiz kirish qonunga zid."