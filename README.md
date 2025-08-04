# WiFi Scanner for Termux

Bu dastur Termux da WiFi tarmoqlarini skanerlash va ularga ulanish uchun yaratilgan.

## O'rnatish

### 1. Termux API o'rnatish
```bash
pkg update && pkg upgrade
pkg install termux-api
```

### 2. Python va kerakli kutubxonalar
```bash
pkg install python
pip install requests
```

### 3. Dasturni yuklab olish
```bash
git clone https://github.com/your-repo/wifi-scanner.git
cd wifi-scanner
```

## Foydalanish

### Oddiy WiFi Scanner (root talab qilmaydi)
```bash
python wifi_scanner.py
```

### Kuchli WiFi Cracker (root talab qiladi)
```bash
# Root huquqlarini olish
su

# Kerakli dasturlarni o'rnatish
pkg install aircrack-ng
pkg install wireless-tools

# Dasturni ishga tushirish
python wifi_cracker.py
```

## Xususiyatlar

### WiFi Scanner (wifi_scanner.py)
- ✅ Root huquqlarini talab qilmaydi
- ✅ WiFi tarmoqlarini skanerlash
- ✅ Tarmoq ma'lumotlarini ko'rsatish (SSID, MAC, signal kuchi)
- ✅ Oddiy parollarni sinab ko'rish
- ✅ Ochiq tarmoqlarni aniqlash

### WiFi Cracker (wifi_cracker.py)
- ⚠️ Root huquqlarini talab qiladi
- 🔓 Monitor rejimi
- 📡 Handshake paketlarini yig'ish
- 🔍 Parol buzish (wordlist bilan)
- 🧹 Avtomatik tozalash

## Natijalar

Dastur ishga tushgandan so'ng:

1. **WiFi tarmoqlarini skanerlaydi**
2. **Tarmoqlar ro'yxatini ko'rsatadi:**
   ```
   1. 🔒 MyWiFi
      MAC: AA:BB:CC:DD:EE:FF | Signal: 📶📶📶 (-45 dBm)
   
   2. 🔓 OpenNetwork
      MAC: 11:22:33:44:55:66 | Signal: 📶📶 (-65 dBm)
   ```

3. **Tarmoq tanlash imkonini beradi**
4. **Parolni sinab ko'radi va natijani ko'rsatadi**

## Xavfsizlik ogohlantirilishi

⚠️ **MUHIM:** Bu dastur faqat o'zingizning tarmoqlaringizni test qilish uchun ishlatilishi kerak. Boshqalarning WiFi tarmoqlariga ruxsatsiz kirish qonuniy emas va jinoiy javobgarlikni o'z ichiga oladi.

## Yordam

Agar muammolar bo'lsa:

1. **Termux API o'rnatilganligini tekshiring**
2. **Root huquqlarini tekshiring (agar kerak bo'lsa)**
3. **WiFi yoqilganligini tekshiring**
4. **Dastur yangilanganligini tekshiring**

## Litsenziya

Bu dastur faqat ta'lim maqsadlarida yaratilgan. Foydalanishda qonuniy javobgarlik sizning zimmingizda.
