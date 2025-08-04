# WiFi Parol Aniqlash Dasturi 🌐

Termux orqali WiFi tarmoqlarini skanerlash va parollarini aniqlash uchun Python dasturi.

## 📋 Xususiyatlar

- ✅ WiFi tarmoqlarini avtomatik skanerlash
- ✅ Topilgan tarmoqlarni raqamlar bilan ko'rsatish (1, 2, 3...)
- ✅ Tanlangan WiFi uchun parol aniqlash
- ✅ Saqlangan parollarni ko'rish
- ✅ Dictionary attack usuli
- ✅ Uzbek tilida interfeys

## 🚀 O'rnatish

### 1. Termux-ni tayyorlash

```bash
# Termux-ni yangilash
pkg update && pkg upgrade

# Git o'rnatish (agar yo'q bo'lsa)
pkg install git

# Bu loyihani yuklab olish
git clone <repository_url>
cd wifi-password-finder
```

### 2. Avtomatik o'rnatish

```bash
# O'rnatish skriptini ishga tushirish
chmod +x setup.sh
./setup.sh
```

### 3. Qo'lda o'rnatish

```bash
# Kerakli paketlarni o'rnatish
pkg install python python-pip wireless-tools wpa-supplicant aircrack-ng root-repo iproute2

# Ruxsatlar berish
chmod +x wifi_scanner.py
```

## 🎯 Ishlatish

### Dasturni ishga tushirish

```bash
# Birinchi usul
./run_wifi_scanner.sh

# Ikkinchi usul
python3 wifi_scanner.py
```

### Root ruxsatini olish

WiFi skanerlash uchun root ruxsati kerak:

```bash
# Su o'rnatish (agar yo'q bo'lsa)
pkg install tsu

# Root bo'lish
tsu
# yoki
su
```

## 📱 Dastur interfeysi

Dastur ishga tushgach quyidagi menyu ko'rinadi:

```
🌐 WiFi Parol Aniqlash Dasturi
========================================

📋 Menyu:
1. WiFi tarmoqlarini qidirish
2. Saqlangan parollarni ko'rish
3. Chiqish

Tanlang (1-3):
```

### 1. WiFi tarmoqlarini qidirish

Bu tanlovni bosganingizda:

1. Dastur WiFi tarmoqlarini skanerlaydi
2. Topilgan tarmoqlar raqamlar bilan ko'rsatiladi:

```
📡 Topilgan WiFi tarmoqlari:
------------------------------------------------------------
#   Nom                       Signal     Shifrlash
------------------------------------------------------------
1   MegaLine_WiFi            45/70      WPA2
2   UzbekTelecom_5G          38/70      WPA2
3   AndroidAP                52/70      WPA
4   Guest_Network            28/70      Open
------------------------------------------------------------

Qaysi WiFi tarmoqni tanlaysiz? (raqam kiriting):
```

3. Raqam kiritganingizdan so'ng parol aniqlash jarayoni boshlanadi

### 2. Saqlangan parollarni ko'rish

Telefonda avval ulangan WiFi tarmoqlarning parollarini ko'rsatadi.

## 🔐 Parol aniqlash usullari

### Dictionary Attack

Dastur quyidagi parollarni sinab ko'radi:

- **Umumiy parollar**: password, 123456789, admin, qwerty, va hokazo
- **Tarmoq nomi asosidagi parollar**: 
  - Tarmoq nomi + "123"
  - Tarmoq nomi + "password" 
  - Tarmoq nomining kichik/katta harflari

### Saqlangan parollar

Quyidagi fayllardagi saqlangan parollarni qidiradi:
- `/data/misc/wifi/wpa_supplicant.conf`
- `/data/wifi/bcm_supp.conf`
- `/system/etc/wifi/wpa_supplicant.conf`

## ⚠️ Muhim ogohlantirishlar

1. **Huquqiy jihat**: Faqat o'zingizga tegishli WiFi tarmoqlarini sinang
2. **Root ruxsati**: WiFi skanerlash uchun root kerak
3. **Ta'lim maqsadi**: Bu dastur faqat ta'lim va xavfsizlik testlari uchun
4. **Javobgarlik**: Noto'g'ri foydalanish uchun dastur muallifi javobgar emas

## 🛠️ Texnik ma'lumotlar

### Kerakli paketlar

- **python3**: Asosiy dasturlash tili
- **wireless-tools**: WiFi skanerlash (iwlist)
- **wpa-supplicant**: WiFi ulanish
- **aircrack-ng**: WiFi xavfsizlik testlari
- **iproute2**: Tarmoq interfeyslari boshqaruvi

### Fayl tuzilishi

```
wifi-password-finder/
├── wifi_scanner.py      # Asosiy dastur
├── setup.sh            # O'rnatish skripti
├── run_wifi_scanner.sh # Ishga tushirish skripti
└── README.md           # Qo'llanma
```

## 🐛 Muammolarni hal qilish

### "Permission denied" xatosi

```bash
# Root ruxsati oling
tsu
# yoki
su
```

### "Command not found" xatosi

```bash
# Paketlarni qayta o'rnating
./setup.sh
```

### WiFi tarmoqlar topilmaydi

```bash
# WiFi interfaysini yoqing
ip link set wlan0 up

# Boshqa interfeys nomini sinab ko'ring
iwconfig
```

### Parol topilmaydi

- Kuchliroq so'zlik ishlatish kerak
- Boshqa usullarni qo'llash (brute force, va hokazo)
- Tarmoq egasidan so'rash

## 📞 Yordam

Agar muammolar bo'lsa:

1. Root ruxsati borligini tekshiring
2. Barcha paketlar o'rnatilganini tekshiring
3. WiFi yoqilganini tekshiring
4. Internet ulanishi borligini tekshiring

## 🔒 Xavfsizlik

Bu dastur faqat quyidagi maqsadlarda ishlatilishi kerak:

- ✅ O'z WiFi tarmoqlaringizni sinash
- ✅ Xavfsizlik testlari (ruxsat bilan)
- ✅ Ta'lim va o'rganish
- ❌ Begona WiFi buzish
- ❌ Noqonuniy kirish

---

**Eslatma**: Bu dastur ta'lim maqsadida yaratilgan. Noto'g'ri foydalanish qonunga xilofdir!
