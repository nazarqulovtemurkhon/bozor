#!/bin/bash
# Quick Install Script for WiFi Password Cracker

echo "🔓 WiFi Password Cracker - Tez o'rnatish"
echo "========================================"

# Check if running in Termux
if [ ! -d "/data/data/com.termux" ]; then
    echo "❌ Bu dastur faqat Termux da ishlaydi!"
    echo "📱 Termux ni Google Play Store dan yuklab oling"
    exit 1
fi

echo "✅ Termux muhiti aniqlandi"

# Update packages
echo "📦 Paketlar yangilanmoqda..."
pkg update -y

# Install Python if not installed
if ! command -v python3 &> /dev/null; then
    echo "🐍 Python o'rnatilmoqda..."
    pkg install -y python
else
    echo "✅ Python allaqachon o'rnatilgan"
fi

# Make scripts executable
echo "🔧 Dasturlar tayyorlanmoqda..."
chmod +x wifi_cracker.py
chmod +x wifi_cracker_termux.py

echo ""
echo "✅ O'rnatish tugallandi!"
echo ""
echo "🚀 Dasturni ishga tushirish:"
echo "   python3 wifi_cracker_termux.py"
echo ""
echo "📋 Yoki:"
echo "   ./wifi_cracker_termux.py"
echo ""
echo "⚠️  Eslatma: Faqat o'zingizning tarmoqlaringizda ishlating!"