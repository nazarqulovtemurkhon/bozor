#!/bin/bash

echo "🚀 WiFi Parol Aniqlash Dasturi - O'rnatish"
echo "=========================================="

# Update package repositories
echo "📦 Paket bazasini yangilash..."
pkg update -y
pkg upgrade -y

# Install required packages
echo "🔧 Kerakli dasturlarni o'rnatish..."
pkg install -y python python-pip
pkg install -y wireless-tools
pkg install -y wpa-supplicant
pkg install -y aircrack-ng
pkg install -y root-repo
pkg install -y iproute2

# Install Python dependencies (if any additional are needed)
echo "🐍 Python kutubxonalarini o'rnatish..."
pip install --upgrade pip

# Give execute permission to the main script
chmod +x wifi_scanner.py

# Create a simple launcher script
cat > run_wifi_scanner.sh << 'EOF'
#!/bin/bash
clear
echo "🌐 WiFi Parol Aniqlash Dasturi ishga tushirilmoqda..."
echo ""
python3 wifi_scanner.py
EOF

chmod +x run_wifi_scanner.sh

echo ""
echo "✅ O'rnatish muvaffaqiyatli tugadi!"
echo ""
echo "🎯 Dasturni ishga tushirish:"
echo "   ./run_wifi_scanner.sh"
echo "   yoki"
echo "   python3 wifi_scanner.py"
echo ""
echo "⚠️  Muhim eslatmalar:"
echo "   • WiFi skanerlash uchun root ruxsati kerak"
echo "   • Su yoki tsu buyrug'i orqali root bo'ling"
echo "   • Faqat o'zingizga tegishli WiFi tarmoqlarini sinang"
echo "   • Bu dastur faqat ta'lim maqsadida yaratilgan"
echo ""