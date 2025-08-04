#!/bin/bash

echo "🚀 Termux WiFi Scanner setup boshlandi..."
echo "======================================"

# Package manager-ni yangilash
echo "📦 Package manager yangilanmoqda..."
pkg update -y
pkg upgrade -y

# Kerakli paketlarni o'rnatish
echo "🔧 Kerakli paketlar o'rnatilmoqda..."
pkg install -y python
pkg install -y python-pip
pkg install -y termux-api
pkg install -y wireless-tools
pkg install -y root-repo
pkg install -y wget
pkg install -y curl

# Python kutubxonalarini o'rnatish
echo "🐍 Python kutubxonalari o'rnatilmoqda..."
pip install --upgrade pip

# Termux API ni sozlash
echo "🔑 Termux API ruxsatlari..."
echo "Iltimos, Android sozlamalarida Termux-ga quyidagi ruxsatlarni bering:"
echo "- Location (Joylashuv)"
echo "- Phone (Telefon)"
echo "- Storage (Xotira)"
echo ""
echo "Termux API ruxsatlarini berish uchun:"
termux-setup-storage

# WiFi scanner faylni ishga tushirishga tayyor qilish
chmod +x wifi_scanner.py

echo ""
echo "✅ O'rnatish tugallandi!"
echo ""
echo "🎯 Ishlatish:"
echo "   python wifi_scanner.py"
echo ""
echo "⚠️  Muhim eslatmalar:"
echo "   1. Android sozlamalarida Termux-ga barcha ruxsatlarni bering"
echo "   2. WiFi yoqilgan bo'lishini tekshiring"
echo "   3. Root ruxsat kerak bo'lishi mumkin"
echo ""
echo "📱 Qo'shimcha ruxsatlar uchun:"
echo "   - Android Settings > Apps > Termux > Permissions"
echo "   - Barcha ruxsatlarni yoqing"