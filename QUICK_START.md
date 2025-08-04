# 🚀 Tezkor Boshlash Qo'llanmasi

## Demo versiyani sinab ko'rish

Demo versiya root ruxsatisiz ishlaydi va haqiqiy WiFi skanermaydi:

```bash
python3 demo_wifi_scanner.py
```

## Haqiqiy dasturni o'rnatish

### 1. Termux tayyorlash
```bash
pkg update && pkg upgrade
```

### 2. O'rnatish
```bash
chmod +x setup.sh
./setup.sh
```

### 3. Root ruxsati olish
```bash
pkg install tsu
tsu
```

### 4. Ishga tushirish
```bash
python3 wifi_scanner.py
```

## Fayllar

- `demo_wifi_scanner.py` - Root ruxsatisiz demo
- `wifi_scanner.py` - Haqiqiy WiFi skanerlar
- `setup.sh` - O'rnatish skripti
- `README.md` - To'liq qo'llanma

## Qisqa misol

1. **Demo sinash**: `python3 demo_wifi_scanner.py`
2. **1-tanlov**: WiFi qidirish
3. **Raqam kiriting**: Masalan `5` (admin)
4. **Natija**: Parol topiladi: `admin`

## Ogohlantirishlar

⚠️ **Faqat o'z WiFi tarmoqlaringizni sinang!**
⚠️ **Ta'lim maqsadida foydalaning!**
⚠️ **Noqonuniy ishlatish taqiqlanadi!**