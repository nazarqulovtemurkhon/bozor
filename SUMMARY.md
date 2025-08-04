# 🌐 WiFi Password Cracker - Yakuniy hisobot

## 📋 Yaratilgan fayllar

### 1. Asosiy dasturlar
- **`wifi_cracker.py`** - Oddiy WiFi parol aniqlash dasturi
- **`wifi_scanner_advanced.py`** - Kengaytirilgan WiFi skaner va parol aniqlash
- **`wifi_demo.py`** - Demo versiya (haqiqiy WiFi hardware talab qilmaydi)

### 2. O'rnatish va ishga tushirish
- **`install.sh`** - Avtomatik o'rnatish skripti
- **`run.sh`** - Dasturni ishga tushirish uchun launcher
- **`requirements.txt`** - Kerakli dasturlar ro'yxati

### 3. Hujjatlar
- **`README.md`** - Batafsil o'rnatish va foydalanish ko'rsatmalari
- **`SUMMARY.md`** - Bu fayl

## 🚀 Tezkor boshlash

### 1. O'rnatish
```bash
# O'rnatish skriptini ishga tushiring
bash install.sh
```

### 2. Dasturni ishga tushirish
```bash
# Launcher orqali
bash run.sh

# Yoki to'g'ridan-to'g'ri
python3 wifi_demo.py        # Demo versiya
python3 wifi_cracker.py     # Oddiy versiya
python3 wifi_scanner_advanced.py  # Kengaytirilgan versiya
```

## 📊 Dastur xususiyatlari

### Demo versiya (`wifi_demo.py`)
- ✅ Hech qanday WiFi hardware talab qilmaydi
- ✅ Sinab ko'rish uchun mo'ljallangan
- ✅ 5 ta demo WiFi tarmoq ko'rsatadi
- ✅ Parol aniqlash jarayonini simulyatsiya qiladi

### Oddiy versiya (`wifi_cracker.py`)
- ✅ WiFi tarmoqlarini qidirish
- ✅ Tarmoq ma'lumotlarini ko'rsatish
- ✅ Parol aniqlash uchun dictionary attack
- ✅ O'zbekcha parollar bazasi

### Kengaytirilgan versiya (`wifi_scanner_advanced.py`)
- ✅ Monitor mode orqali kuchli skaner
- ✅ Signal kuchi bo'yicha saralash
- ✅ Ko'p usulli parol aniqlash
- ✅ WPS va Deauth hujumlari
- ✅ Batafsil natijalar

## 🔧 Texnik talablar

### Termux uchun kerakli dasturlar
- `python3` - Python dasturlash tili
- `aircrack-ng` - WiFi xavfsizlik dasturlari
- `wireless-tools` - WiFi interfeyslari bilan ishlash
- `git` - Kodlarni yuklab olish
- `wget` - Fayllarni yuklab olish

### Python paketlari
- `colorama` - Rangli matnlar
- `requests` - HTTP so'rovlar

## 📱 Foydalanish ko'rsatmalari

### 1. Demo versiya bilan boshlash
```bash
python3 wifi_demo.py
```
Bu sizga dastur qanday ishlashini ko'rsatadi.

### 2. Haqiqiy WiFi bilan ishlash
```bash
# Root huquqlarini olish
su

# Dasturni ishga tushirish
python3 wifi_cracker.py
```

### 3. Kengaytirilgan funksiyalar
```bash
python3 wifi_scanner_advanced.py
```

## ⚠️ Muhim eslatmalar

1. **Qonuniy foydalanish** - Faqat o'zingizning tarmoqlaringizda ishlatish
2. **Root huquqlari** - Haqiqiy WiFi skaner uchun root kerak
3. **Xavfsizlik** - Boshqalarning WiFi parollarini buzish qonunga zid
4. **Ta'lim maqsadi** - Bu dastur faqat ta'lim uchun yaratilgan

## 🎯 Natijalar

Dastur ishga tushganda:
1. WiFi tarmoqlarini qidiradi
2. Tarmoqlar ro'yxatini ko'rsatadi (№, SSID, BSSID, Kanal, Shifrlash)
3. Tanlangan tarmoq parolini aniqlashga harakat qiladi
4. Natijalarni faylga saqlaydi

## 📞 Yordam

Agar muammolar bo'lsa:
1. `README.md` faylini o'qing
2. `bash install.sh` buyrug'ini bajaring
3. Root huquqlarini tekshiring (`su`)
4. WiFi yoqilganligini tekshiring

---
**Eslatma:** Bu dastur faqat ta'lim va o'z tarmoqlaringizni sinab ko'rish uchun mo'ljallangan. Boshqalarning WiFi parollarini buzish qonunga zid va jinoiy javobgarlikni o'z ichiga oladi.