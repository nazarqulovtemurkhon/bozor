# 🔓 WiFi Password Cracker - Termux uchun

Bu dastur Termux da WiFi tarmoqlarini skanerlaydi va parollarini aniqlashga harakat qiladi.

## 📋 Xususiyatlar

- ✅ WiFi tarmoqlarini avtomatik skanerlash
- 📊 Tarmoqlar ro'yxatini ko'rsatish (SSID, BSSID, Channel, Encryption)
- 🔓 Parolni aniqlash uchun wordlist yordamida urinish
- 🎯 Qulay interfeys va o'zbek tilida
- ⚡ Tez va samarali ishlash

## 🛠️ O'rnatish

### 1. Termux ni o'rnatish
Agar Termux o'rnatilmagan bo'lsa, Google Play Store dan yuklab oling.

### 2. Dasturni yuklab olish
```bash
git clone https://github.com/your-username/wifi-cracker.git
cd wifi-cracker
```

### 3. O'rnatish skriptini ishga tushirish
```bash
chmod +x setup.sh
./setup.sh
```

### 4. Qo'lda o'rnatish (agar skript ishlamasa)
```bash
# Paketlarni yangilash
pkg update && pkg upgrade

# Kerakli dasturlarni o'rnatish
pkg install python
pkg install aircrack-ng
pkg install wireless-tools

# Dasturni ishga tushirish uchun tayyorlash
chmod +x wifi_cracker.py
```

## 🚀 Foydalanish

### Dasturni ishga tushirish
```bash
python wifi_cracker.py
```

### Asosiy funksiyalar

1. **WiFi tarmoqlarini skanerlash**
   - Dastur avtomatik ravishda mavjud WiFi tarmoqlarini topadi
   - Har bir tarmoq haqida ma'lumot ko'rsatadi

2. **Tarmoq tanlash**
   - Ro'yxatdan kerakli tarmoqni tanlang
   - Raqam kiriting (1, 2, 3, ...)

3. **Parolni aniqlash**
   - Dastur tanlangan tarmoq parolini aniqlashga harakat qiladi
   - Wordlist yordamida turli parollar tekshiriladi

## 📊 Natijalar

Dastur quyidagi ma'lumotlarni ko'rsatadi:
- **SSID**: Tarmoq nomi
- **BSSID**: Tarmoq MAC manzili
- **Channel**: Tarmoq kanali
- **Encrypted**: Shifrlangan yoki yo'q

## ⚠️ Muhim eslatmalar

- 🔒 Bu dastur faqat o'zingizning tarmoqlaringizda ishlatilishi kerak
- 🚫 Boshqalarning tarmoqlariga ruxsatsiz kirish qonunga zid
- ⚖️ Foydalanuvchi javobgarlikda
- 🎯 Parol topilish kafolati yo'q

## 🛠️ Texnik ma'lumotlar

- **Platforma**: Termux (Android)
- **Til**: Python 3
- **Kerakli dasturlar**: aircrack-ng, wireless-tools
- **Fayl**: wifi_cracker.py

## 🔧 Xatoliklar va yechimlar

### "WiFi interfeysi topilmadi" xatosi
```bash
# WiFi yoqilganligini tekshiring
termux-wifi-enable

# Yoki
termux-wifi-scaninfo
```

### "Dastur o'rnatilmagan" xatosi
```bash
# Qaytadan o'rnatish
pkg install aircrack-ng
pkg install wireless-tools
```

### Root huquqlari kerakmi?
- Root huquqlari talab qilinmaydi
- Termux da oddiy foydalanuvchi huquqlari yetarli

## 📞 Yordam

Agar muammolar yuzaga kelsa:
1. README faylini o'qing
2. Dastur ichidagi yordam bo'limini ko'ring
3. GitHub da issue oching

## 📄 Litsenziya

Bu dastur faqat ta'lim maqsadida yaratilgan. Foydalanishda qonuniy javobgarlik foydalanuvchida.

---

**⚠️ Eslatma**: Bu dastur faqat o'zingizning tarmoqlaringizda ishlatilishi kerak!
