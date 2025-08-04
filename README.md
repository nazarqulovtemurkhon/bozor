# 🌐 WiFi Password Cracker for Termux

Bu dastur Termux orqali WiFi tarmoqlarini skaner qilish va ularning parollarini aniqlash uchun yaratilgan.

## 📋 Xususiyatlar

- ✅ WiFi tarmoqlarini avtomatik qidirish
- 📶 Tarmoq ma'lumotlarini ko'rsatish (SSID, BSSID, Kanal, Shifrlash)
- 🔑 Parol aniqlash uchun turli usullar
- 🇺🇿 O'zbekcha parollar bazasi
- 💾 Natijalarni faylga saqlash
- 🎯 Foydalanuvchi do'stona interfeys

## 🚀 O'rnatish

### 1. Termux o'rnatish
Agar Termux o'rnatilmagan bo'lsa, uni Google Play Store dan yuklab oling.

### 2. Kerakli dasturlarni o'rnatish
```bash
# O'rnatish skriptini ishga tushiring
bash install.sh
```

Yoki qo'lda o'rnatish:
```bash
# Paketlarni yangilash
pkg update && pkg upgrade

# Kerakli dasturlarni o'rnatish
pkg install python aircrack-ng wireless-tools git wget

# Python paketlarini o'rnatish
pip install colorama requests
```

### 3. Root huquqlarini olish
```bash
# Root bo'lish
su
```

## 📖 Foydalanish

### Oddiy versiya
```bash
python wifi_cracker.py
```

### Kengaytirilgan versiya
```bash
python wifi_scanner_advanced.py
```

## 🔧 Dastur ishlash tartibi

1. **Dasturlarni tekshirish** - Kerakli dasturlar o'rnatilganligini tekshiradi
2. **Interfeys tanlash** - WiFi interfeysini tanlaydi
3. **Tarmoqlarni qidirish** - Atrofidagi WiFi tarmoqlarini topadi
4. **Tarmoq tanlash** - Parolini aniqlash kerak bo'lgan tarmoqni tanlaydi
5. **Parol aniqlash** - Turli usullar bilan parolni sinab ko'radi
6. **Natijalarni saqlash** - Natijalarni faylga saqlaydi

## 📊 Ko'rsatiladigan ma'lumotlar

- **№** - Tarmoq tartib raqami
- **SSID** - Tarmoq nomi
- **BSSID** - Tarmoq MAC manzili
- **Channel** - Tarmoq kanali
- **Encryption** - Shifrlash turi (WEP/WPA/WPA2)
- **Signal** - Signal kuchi

## 🔑 Parol aniqlash usullari

1. **Keng tarqalgan parollar** - 12345678, password, admin va boshqalar
2. **O'zbekcha parollar** - uzbekistan, tashkent, samarkand va boshqalar
3. **Raqamli patternlar** - Yillar, telefon raqamlar va boshqalar
4. **WPS hujum** - WPS yoqilgan routerlar uchun
5. **Deauthentication hujum** - Boshqa foydalanuvchilarni uzib qo'yish

## ⚠️ Muhim eslatmalar

- ❌ Bu dasturni faqat o'zingizning tarmoqlaringizda ishlatish mumkin
- 🔒 Boshqalarning WiFi parollarini buzish qonunga zid
- 📱 Root huquqlari kerak
- ⏱️ Parol aniqlash uzoq vaqt olishi mumkin

## 📁 Fayl tuzilishi

```
wifi-cracker/
├── wifi_cracker.py          # Oddiy versiya
├── wifi_scanner_advanced.py # Kengaytirilgan versiya
├── install.sh              # O'rnatish skripti
├── requirements.txt        # Kerakli dasturlar
└── README.md              # Bu fayl
```

## 🛠️ Xatoliklar va yechimlar

### "Hech qanday WiFi tarmoq topilmadi"
- WiFi yoqilganligini tekshiring
- Root huquqlarini oling (`su`)
- Interfeys to'g'ri tanlanganligini tekshiring

### "Dastur o'rnatilmagan"
- `bash install.sh` buyrug'ini bajaring
- Yoki qo'lda o'rnatish ko'rsatmalarini bajaring

### "Root huquqlari kerak"
- `su` buyrug'i bilan root bo'ling
- Yoki Termux'da root huquqlarini yoqing

## 📞 Yordam

Agar muammolar bo'lsa:
1. README faylini diqqat bilan o'qing
2. Xatolik xabarini ko'rsating
3. Termux versiyangizni tekshiring

## 📄 Litsenziya

Bu dastur faqat ta'lim maqsadida yaratilgan. Faqat o'zingizning tarmoqlaringizda ishlatish mumkin.

---
**Eslatma:** Bu dastur faqat ta'lim va o'z tarmoqlaringizni sinab ko'rish uchun mo'ljallangan. Boshqalarning WiFi parollarini buzish qonunga zid va jinoiy javobgarlikni o'z ichiga oladi.
