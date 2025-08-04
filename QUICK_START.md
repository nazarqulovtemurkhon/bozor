# 🚀 Tezkor Boshlash

## 1. O'rnatish (5 daqiqa)

```bash
# 1. Termux ni oching
# 2. Quyidagi buyruqlarni kiriting:

pkg update && pkg upgrade
pkg install python termux-api
pip install requests

# 3. Dasturni yuklab oling (agar git mavjud bo'lsa)
git clone https://github.com/your-repo/wifi-scanner.git
cd wifi-scanner

# Yoki fayllarni qo'lda yuklab oling
```

## 2. Test qilish

```bash
python test_wifi.py
```

Agar barcha testlar muvaffaqiyatli bo'lsa, dastur ishlatishga tayyor!

## 3. Ishlatish

### Oddiy skaner (root talab qilmaydi)
```bash
python wifi_scanner.py
```

### Kuchli cracker (root talab qiladi)
```bash
su
pkg install aircrack-ng wireless-tools
python wifi_cracker.py
```

## 4. Natija

Dastur ishga tushgandan so'ng:

1. **WiFi tarmoqlarini skanerlaydi**
2. **Ro'yxatni ko'rsatadi:**
   ```
   1. 🔒 MyWiFi
      MAC: AA:BB:CC:DD:EE:FF | Signal: 📶📶📶 (-45 dBm)
   
   2. 🔓 OpenNetwork  
      MAC: 11:22:33:44:55:66 | Signal: 📶📶 (-65 dBm)
   ```
3. **Tarmoq tanlash imkonini beradi**
4. **Parolni sinab ko'radi**

## ⚠️ Muhim

- Bu dastur faqat o'zingizning tarmoqlaringizni test qilish uchun!
- Boshqalarning WiFi ga ruxsatsiz kirish qonuniy emas!
- Faqat ta'lim maqsadlarida ishlatish kerak!

## 🆘 Yordam

Agar muammolar bo'lsa:
1. `python test_wifi.py` ni ishga tushiring
2. README.md faylini o'qing
3. Termux API o'rnatilganligini tekshiring