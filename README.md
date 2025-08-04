# 📡 Termux WiFi Scanner & Password Finder

Bu dastur Termux orqali WiFi tarmoqlarini skanlab, ularning parollarini aniqlashga yordam beradi.

## 🚀 O'rnatish

### 1. Setup skriptini ishga tushiring:
```bash
chmod +x setup.sh
./setup.sh
```

### 2. Yoki qo'lda o'rnatish:
```bash
# Paketlarni yangilash
pkg update && pkg upgrade

# Kerakli paketlar
pkg install python termux-api wireless-tools

# Ruxsatlarni berish
termux-setup-storage
```

## 🎯 Ishlatish

### Asosiy dasturni ishga tushirish:
```bash
python wifi_scanner.py
```

### Nima qiladi:
1. 📡 Atrofdagi WiFi tarmoqlarini skanlar
2. 📋 1, 2, 3... tartib raqamlari bilan ko'rsatadi
3. 🎯 Kerakli WiFi raqamini tanlaysiz
4. 🔍 Parolni aniqlashga harakat qiladi

## ⚙️ Xususiyatlar

- ✅ WiFi tarmoqlarini skanlar
- ✅ Signal quvvati va xavfsizlik turini ko'rsatadi
- ✅ Saqlangan parollarni tekshiradi
- ✅ Umumiy parollarni sinab ko'radi
- ✅ Foydalanuvchi-do'st interfeys

## 📋 Chiqish namunasi

```
🌐 MAVJUD WiFi TARMOQLARI
============================================================
No.  SSID                     Signal      Security       
------------------------------------------------------------
1    MyHome_WiFi              -45 dBm     WPA2          
2    Neighbor_5G              -67 dBm     WPA3          
3    CafeWiFi                 -52 dBm     Open          
4    Office_Guest             -71 dBm     WPA2          

Tanlang (raqam kiriting yoki 'q' - chiqish): 1

🎯 Tanlangan: MyHome_WiFi
==============================
✅ Saqlangan parol topildi: mypassword123
```

## ⚠️ Muhim eslatmalar

### Ruxsatlar:
1. **Android Settings** > **Apps** > **Termux** > **Permissions**
2. Quyidagi ruxsatlarni yoqing:
   - 📍 Location (Joylashuv)
   - 📞 Phone (Telefon) 
   - 💾 Storage (Xotira)

### Qo'shimcha:
- 🔋 WiFi yoqilgan bo'lishi kerak
- 📶 Internet ulanishi tavsiya etiladi
- 🛡️ Ba'zi funksiyalar uchun root kerak

## 🔧 Muammolarni hal qilish

### WiFi topilmasa:
```bash
# Termux API-ni qayta o'rnatish
pkg install termux-api

# Ruxsatlarni qayta berish
termux-setup-storage
```

### Root kerak bo'lsa:
```bash
# Magisk yoki SuperSU orqali root oling
# Yoki Termux:Boot ishlatib ko'ring
```

## 🛡️ Xavfsizlik haqida

⚠️ **Diqqat**: Bu dastur faqat ta'lim maqsadida yaratilgan!

- ✅ Faqat o'z WiFi tarmoqlaringizda ishlating
- ❌ Boshqalarning WiFi parollarini buzishga urinmang
- 🚫 Noqonuniy maqsadlarda ishlatmang

## 📞 Yordam

Muammo bo'lsa yoki savollar bo'lsa:
- GitHub Issues orqali yozing
- Kodni o'rganib ko'ring
- Termux documentation ni tekshiring

## 📄 Litsenziya

Bu dastur ochiq kod bo'lib, faqat ta'lim maqsadida ishlatilsin!

---
**Eslatma**: WiFi parollarini topish doimo ishlamasligi mumkin. Bu normal holat!
