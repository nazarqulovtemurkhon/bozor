#!/bin/bash
# WiFi Password Cracker Launcher
# Author: Assistant

echo "🌐 WiFi Password Cracker"
echo "========================"
echo ""
echo "Qaysi versiyani ishga tushirish kerak?"
echo "1. Demo versiya (wifi_demo.py) - Sinab ko'rish uchun"
echo "2. Oddiy versiya (wifi_cracker.py)"
echo "3. Kengaytirilgan versiya (wifi_scanner_advanced.py)"
echo "4. Chiqish"
echo ""

while true; do
    read -p "Tanlang (1-4): " choice
    
    case $choice in
        1)
            echo "🚀 Demo versiya ishga tushirilmoqda..."
            python3 wifi_demo.py
            break
            ;;
        2)
            echo "🚀 Oddiy versiya ishga tushirilmoqda..."
            python3 wifi_cracker.py
            break
            ;;
        3)
            echo "🚀 Kengaytirilgan versiya ishga tushirilmoqda..."
            python3 wifi_scanner_advanced.py
            break
            ;;
        4)
            echo "👋 Xayr!"
            exit 0
            ;;
        *)
            echo "❌ Noto'g'ri tanlov! Qaytadan kiriting."
            ;;
    esac
done