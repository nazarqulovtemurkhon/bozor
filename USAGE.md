# 🔓 WiFi Password Cracker - Foydalanish ko'rsatmasi

## 📱 Termux da ishlatish

### 1. Termux ni o'rnatish
- Google Play Store dan Termux ni yuklab oling
- Yoki F-Droid dan Termux ni o'rnating

### 2. Dasturni yuklab olish
```bash
# Git yordamida yuklab olish
git clone https://github.com/your-username/wifi-cracker.git
cd wifi-cracker

# Yoki fayllarni qo'lda ko'chirish
```

### 3. O'rnatish
```bash
# Tez o'rnatish
./install.sh

# Yoki qo'lda o'rnatish
pkg update && pkg upgrade
pkg install python
chmod +x wifi_cracker_termux.py
```

### 4. Dasturni ishga tushirish
```bash
python3 wifi_cracker_termux.py
```

## 🎯 Foydalanish tartibi

### 1. Asosiy menyu
```
📋 Asosiy menyu:
1. 🔍 WiFi tarmoqlarini skanerlash
2. 📦 Dasturlarni o'rnatish
3. ❓ Yordam ko'rsatish
4. 🚪 Chiqish
```

### 2. Tarmoqlarni skanerlash
- `1` ni tanlang
- Dastur avtomatik ravishda WiFi tarmoqlarini topadi
- Natijalar jadval ko'rinishida ko'rsatiladi

### 3. Tarmoq tanlash
```
📋 Mavjud WiFi tarmoqlari:
================================================================================
№   SSID                BSSID              Channel  Signal   Encrypted
================================================================================
1   HomeWiFi            AA:BB:CC:DD:EE:FF  6        -45      🔒 Ha
2   Office_Network      11:22:33:44:55:66  11       -52      🔒 Ha
3   Guest_WiFi          AA:11:BB:22:CC:33  1        -60      🔓 Yo'q
4   Neighbor_5G         DD:44:EE:55:FF:66  36       -48      🔒 Ha
5   Cafe_Free_WiFi      77:88:99:AA:BB:CC  9        -65      🔓 Yo'q
================================================================================
```

### 4. Parolni aniqlash
- Kerakli tarmoq raqamini kiriting (1-5)
- Dastur parolni aniqlashga harakat qiladi
- Natija ko'rsatiladi

## 📊 Natijalar tushuntirilishi

- **SSID**: Tarmoq nomi
- **BSSID**: Tarmoq MAC manzili
- **Channel**: Kanal raqami
- **Signal**: Signallar kuchi (dBm)
- **Encrypted**: Shifrlangan yoki yo'q

## ⚠️ Muhim eslatmalar

### ✅ Ruxsat berilgan
- O'zingizning WiFi tarmoqlaringiz
- Sizga tegishli qurilmalar
- Ta'lim maqsadida

### ❌ Ruxsat berilmagan
- Boshqalarning tarmoqlari
- Ruxsatsiz kirish
- Qonunga zid ishlar

## 🔧 Xatoliklar va yechimlar

### "Termux muhiti topilmadi"
```bash
# Termux ni Google Play Store dan yuklab oling
# Yoki F-Droid dan o'rnating
```

### "Python o'rnatilmagan"
```bash
pkg install python
```

### "WiFi tarmoqlari topilmadi"
```bash
# WiFi yoqilganligini tekshiring
# Termux da ruxsatlarni tekshiring
```

### "Parol topilmadi"
- Bu normal holat
- Kuchli parollar qo'llanilgan
- Boshqa tarmoq bilan urinib ko'ring

## 💡 Maslahatlar

### Xavfsizlik uchun
- Kuchli parollar ishlating (8+ belgi)
- WPA3 shifrlash standartini qo'llang
- Muntazam parolni o'zgartiring
- Tarmoq nomini yashiring

### Dastur uchun
- Faqat o'zingizning tarmoqlaringizda ishlating
- Boshqalarga zarar yetkazmang
- Qonuniy chegaralarni saqlang

## 📞 Yordam

Agar muammolar yuzaga kelsa:
1. README.md faylini o'qing
2. Dastur ichidagi yordam bo'limini ko'ring
3. GitHub da issue oching

---

**⚠️ Eslatma**: Bu dastur faqat ta'lim maqsadida yaratilgan!