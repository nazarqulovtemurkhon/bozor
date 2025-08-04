# 🔐 WiFi Password Finder - Termux uchun

Bu dastur WiFi tarmoqlarini skaner qiladi va parollarni topishga harakat qiladi. Faqat o'zingizning tarmoqlaringizda ishlatilishi kerak!

## ⚠️ Muhim ogohlantirish

- Bu dastur faqat o'zingizning WiFi tarmoqlaringizda ishlatilishi kerak
- Boshqalarning WiFi tarmoqlariga ruxsatsiz kirish qonunga zid!
- Faqat o'qish maqsadida ishlatilishi kerak

## 📦 O'rnatish

### 1. Kerakli dasturlarni o'rnatish

```bash
# O'rnatish skriptini ishga tushirish
bash install_dependencies.sh
```

Yoki qo'lda o'rnatish:

```bash
# Termux paketlarini yangilash
pkg update && pkg upgrade

# Kerakli dasturlarni o'rnatish
pkg install python python-pip aircrack-ng wireless-tools net-tools nmap macchanger

# Python kutubxonalarini o'rnatish
pip install colorama requests psutil
```

### 2. Root huquqlarini olish

```bash
# Root bo'lish
su
```

## 🚀 Ishlatish

### Oddiy versiya

```bash
python wifi_password_finder.py
```

### Kuchli versiya

```bash
python advanced_wifi_cracker.py
```

## 📋 Dastur xususiyatlari

### Oddiy versiya (`wifi_password_finder.py`)
- ✅ WiFi tarmoqlarini skaner qilish
- ✅ Tarmoqlar ro'yxatini ko'rsatish
- ✅ Tarmoq tanlash
- ✅ Dictionary hujumi
- ✅ Oddiy parollar ro'yxati

### Kuchli versiya (`advanced_wifi_cracker.py`)
- ✅ Barcha oddiy versiya xususiyatlari
- ✅ WPS Pin hujumi
- ✅ Katta parollar ro'yxati
- ✅ WPA Handshake yig'ish
- ✅ Monitor mode qo'llab-quvvatlash
- ✅ Signal handler'lar
- ✅ Root huquqlarini tekshirish

## 🔓 Hujum usullari

### 1. WPS Pin hujumi
- Eng tez usul
- WPS qo'llab-quvvatlanadigan routerlar uchun
- Reaver dasturi ishlatiladi

### 2. Dictionary hujumi
- Oddiy parollar ro'yxati bilan
- Uzbecha parollar kiritilgan
- Sekin, lekin samarali

### 3. Brute force hujumi
- Barcha mumkin bo'lgan kombinatsiyalar
- Juda sekin
- Faqat kichik parollar uchun

### 4. WPA Handshake yig'ish
- Handshake faylini yig'adi
- Aircrack-ng bilan parolni topish mumkin
- Offline hujum uchun

## 📱 Termux uchun maxsus ko'rsatmalar

### 1. Storage ruxsatini berish
```bash
termux-setup-storage
```

### 2. Root olish (agar kerak bo'lsa)
```bash
# Magisk yoki boshqa root dasturi orqali
```

### 3. WiFi adapter qo'llab-quvvatlashini tekshirish
```bash
iwconfig
```

## 🛠️ Xatoliklarni tuzatish

### "WiFi interfeysi topilmadi" xatosi
```bash
# WiFi adapter mavjudligini tekshirish
ls /sys/class/net/

# WiFi adapter'ni yoqish
ip link set wlan0 up
```

### "Root huquqlari kerak" xatosi
```bash
# Root bo'lish
su

# Yoki Termux'da
pkg install tsu
tsu
```

### "Dastur topilmadi" xatosi
```bash
# Dasturlarni qayta o'rnatish
pkg install aircrack-ng wireless-tools
```

## 📊 Natijalar

Dastur quyidagi ma'lumotlarni ko'rsatadi:
- 📶 Tarmoq nomi (SSID)
- 📍 MAC manzil (BSSID)
- 📡 Kanal raqami
- 📶 Signal kuchlanishi
- 🔓 WPS qo'llab-quvvatlash
- 🔑 Topilgan parol

## 🔧 Sozlash

### Parollar ro'yxatini o'zgartirish
`create_wordlist()` funksiyasini tahrirlang:

```python
def create_wordlist(self):
    wordlist = []
    # O'zingizning parollaringizni qo'shing
    custom_passwords = ['mening_parol', '12345678', ...]
    wordlist.extend(custom_passwords)
    return wordlist
```

### Skaner vaqtini o'zgartirish
```python
# Skaner vaqtini oshirish
time.sleep(5)  # 5 soniya
```

## 📞 Yordam

Agar muammolar bo'lsa:
1. README faylini o'qing
2. Xatolik xabarini ko'ring
3. Dasturlarni qayta o'rnating
4. Root huquqlarini tekshiring

## 📄 Litsenziya

Bu dastur faqat o'qish maqsadida yaratilgan. Boshqalarning WiFi tarmoqlariga ruxsatsiz kirish qonunga zid!

## 🤝 Hissa qo'shish

Dasturni yaxshilash uchun:
1. Fork qiling
2. O'zgarishlarni qiling
3. Pull request yuboring

---

**⚠️ Eslatma:** Bu dastur faqat o'zingizning tarmoqlaringizda ishlatilishi kerak!
