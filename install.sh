#!/bin/bash
# WiFi Password Cracker Installation Script for Termux
# Author: Assistant

echo "🌐 WiFi Password Cracker o'rnatish boshlanmoqda..."
echo "=" * 50

# Update package list
echo "📦 Paketlar ro'yxatini yangilash..."
pkg update -y

# Upgrade packages
echo "⬆️  Paketlarni yangilash..."
pkg upgrade -y

# Install required packages
echo "🔧 Kerakli dasturlarni o'rnatish..."
pkg install -y python
pkg install -y aircrack-ng
pkg install -y wireless-tools
pkg install -y git
pkg install -y wget

# Install Python packages
echo "🐍 Python paketlarini o'rnatish..."
pip install colorama
pip install requests

# Make the script executable
echo "🔐 Fayl huquqlarini o'zgartirish..."
chmod +x wifi_cracker.py

echo ""
echo "✅ O'rnatish tugatildi!"
echo ""
echo "🚀 Dasturni ishga tushirish uchun:"
echo "   python wifi_cracker.py"
echo ""
echo "📋 Eslatma:"
echo "   - WiFi yoqilganligini tekshiring"
echo "   - Root huquqlari kerak bo'lishi mumkin"
echo "   - Faqat o'zingizning tarmoqlaringizda ishlatish mumkin"