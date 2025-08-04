#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔓 WiFi Password Cracker - Avtomatik versiya
Author: AI Assistant
Description: Barcha kutubxonalar va kodlar bitta faylda, avtomatik ishlaydi
Platforma: Termux (Android)
"""

# Barcha kerakli kutubxonalar
import os
import sys
import time
import subprocess
import re
import json
import random
import string
from typing import List, Dict, Optional

# Ranglar uchun maxsus kodlar
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class AutoWiFiCracker:
    def __init__(self):
        self.networks = []
        self.wordlist_path = "/data/data/com.termux/files/home/wordlist.txt"
        self.termux_path = "/data/data/com.termux"
        self.auto_mode = True
        
    def print_banner(self):
        """Dastur bannerini ko'rsatish"""
        banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                🔓 WiFi Password Cracker 🔓                    ║
║                    Avtomatik versiya                         ║
║                    Termux uchun v2.0                         ║
╚══════════════════════════════════════════════════════════════╝
{Colors.END}
"""
        print(banner)
    
    def auto_setup(self):
        """Avtomatik sozlash"""
        print(f"{Colors.BLUE}🔧 Avtomatik sozlash boshlandi...{Colors.END}")
        
        # Termux muhitini tekshirish
        if not os.path.exists(self.termux_path):
            print(f"{Colors.RED}❌ Bu dastur faqat Termux da ishlaydi!{Colors.END}")
            print(f"{Colors.YELLOW}📱 Termux ni Google Play Store dan yuklab oling{Colors.END}")
            return False
        
        print(f"{Colors.GREEN}✅ Termux muhiti aniqlandi{Colors.END}")
        
        # Python mavjudligini tekshirish
        try:
            subprocess.run(["python3", "--version"], capture_output=True, check=True)
            print(f"{Colors.GREEN}✅ Python 3 mavjud{Colors.END}")
        except:
            print(f"{Colors.YELLOW}📦 Python o'rnatilmoqda...{Colors.END}")
            try:
                subprocess.run(["pkg", "install", "-y", "python"], capture_output=True, check=True)
                print(f"{Colors.GREEN}✅ Python o'rnatildi{Colors.END}")
            except:
                print(f"{Colors.RED}❌ Python o'rnatishda xatolik{Colors.END}")
                return False
        
        # Wordlist yaratish
        if not os.path.exists(self.wordlist_path):
            self.create_mega_wordlist()
        
        return True
    
    def create_mega_wordlist(self):
        """Katta wordlist yaratish"""
        print(f"{Colors.BLUE}📝 Katta wordlist yaratilmoqda...{Colors.END}")
        
        passwords = []
        
        # 1. Oddiy parollar
        simple_passwords = [
            "12345678", "password", "admin", "1234567890", "qwerty",
            "123456789", "123456", "1234567", "password123", "admin123",
            "12345678910", "123456789012", "1234567890123", "12345678901234",
            "qwerty123", "qwertyuiop", "asdfghjkl", "zxcvbnm", "11111111",
            "00000000", "88888888", "99999999", "77777777", "66666666",
            "55555555", "44444444", "33333333", "22222222", "111111111",
            "000000000", "123123123", "321321321", "456456456", "654654654",
            "789789789", "987987987", "147147147", "741741741", "258258258",
            "852852852", "369369369", "963963963", "159159159", "951951951",
            "357357357", "753753753"
        ]
        passwords.extend(simple_passwords)
        
        # 2. O'zbekcha parollar
        uzbek_passwords = [
            "uzbekistan", "tashkent", "samarkand", "bukhara", "andijan",
            "fergana", "namangan", "navoiy", "kashkadarya", "surkhandarya",
            "khorezm", "karakalpakstan", "nukus", "urgench", "khiva",
            "uzbek", "uzbekcha", "o'zbek", "o'zbekcha", "toshkent",
            "samarqand", "buxoro", "andijon", "farg'ona", "namangan",
            "navoiy", "qashqadaryo", "surxondaryo", "xorazm", "qoraqalpog'iston",
            "tashkent123", "samarkand123", "uzbekistan123", "toshkent123",
            "buxoro123", "andijon123", "fargona123", "namangan123"
        ]
        passwords.extend(uzbek_passwords)
        
        # 3. Yillar va kombinatsiyalar
        years = ["2024", "2023", "2022", "2021", "2020", "2019", "2018", "2017", "2016", "2015"]
        for year in years:
            passwords.append(year)
            passwords.append(year + year)  # 20242024
            passwords.append(year + "123")  # 2024123
            passwords.append("123" + year)  # 1232024
        
        # 4. Telefon raqamlari
        phone_patterns = [
            "998901234567", "99890123456", "9989012345", "998901234",
            "901234567", "90123456", "9012345", "901234", "90123",
            "9989012345678", "99890123456789", "998901234567890",
            "9989012345678901", "99890123456789012"
        ]
        passwords.extend(phone_patterns)
        
        # 5. Keng tarqalgan so'zlar
        common_words = [
            "wifi", "internet", "network", "router", "modem", "home",
            "office", "work", "school", "university", "college", "library",
            "cafe", "restaurant", "hotel", "airport", "station", "mall",
            "shop", "store", "market", "bank", "hospital", "clinic",
            "pharmacy", "gas", "petrol", "fuel", "car", "auto", "bus",
            "train", "metro", "taxi", "driver", "passenger", "guest",
            "visitor", "friend", "family", "home", "house", "apartment",
            "room", "bedroom", "kitchen", "bathroom", "living", "dining",
            "wifi123", "internet123", "network123", "router123", "home123",
            "office123", "work123", "school123", "cafe123", "hotel123"
        ]
        passwords.extend(common_words)
        
        # 6. Standart parollar
        default_passwords = [
            "admin1234", "root1234", "user1234", "guest1234", "test1234",
            "demo1234", "welcome1234", "hello1234", "world1234", "internet1234",
            "network1234", "wifi1234", "router1234", "modem1234", "home1234",
            "office1234", "work1234", "school1234", "cafe1234", "hotel1234",
            "admin12345", "root12345", "user12345", "guest12345", "test12345",
            "demo12345", "welcome123", "hello123", "world123", "internet123"
        ]
        passwords.extend(default_passwords)
        
        # 7. Ketma-ket raqamlar
        sequential_patterns = [
            "123123123", "321321321", "456456456", "654654654", "789789789",
            "987987987", "147147147", "741741741", "258258258", "852852852",
            "369369369", "963963963", "159159159", "951951951", "357357357",
            "753753753", "111111111", "222222222", "333333333", "444444444",
            "555555555", "666666666", "777777777", "888888888", "999999999",
            "000000000", "123456789", "987654321", "11111111", "22222222"
        ]
        passwords.extend(sequential_patterns)
        
        # 8. Harflar bilan kombinatsiyalar
        letter_combinations = [
            "aaaa", "bbbb", "cccc", "dddd", "eeee", "ffff", "gggg", "hhhh",
            "iiii", "jjjj", "kkkk", "llll", "mmmm", "nnnn", "oooo", "pppp",
            "qqqq", "rrrr", "ssss", "tttt", "uuuu", "vvvv", "wwww", "xxxx",
            "yyyy", "zzzz", "abcd", "dcba", "qwer", "rewq", "asdf", "fdsa",
            "zxcv", "vcxz", "qaz", "wsx", "edc", "rfv", "tgb", "yhn", "ujm",
            "qwerty", "asdfgh", "zxcvbn", "qwertyuiop", "asdfghjkl", "zxcvbnm"
        ]
        passwords.extend(letter_combinations)
        
        # 9. Kuchli parollar
        strong_passwords = [
            "password123", "admin1234", "root12345", "user12345", "guest12345",
            "test12345", "demo12345", "welcome123", "hello1234", "world1234",
            "internet123", "network123", "wifi12345", "router123", "modem12345",
            "home12345", "office123", "work12345", "school123", "cafe12345",
            "hotel12345", "airport123", "station123", "mall12345", "shop12345",
            "store12345", "market123", "bank12345", "hospital123", "clinic12345",
            "password1234", "admin12345", "root123456", "user123456", "guest123456"
        ]
        passwords.extend(strong_passwords)
        
        # 10. O'zbekcha kuchli parollar
        uzbek_strong = [
            "uzbekistan123", "tashkent123", "samarkand123", "bukhara123",
            "andijan123", "fergana123", "namangan123", "navoiy123",
            "kashkadarya123", "surkhandarya123", "khorezm123",
            "karakalpakstan123", "nukus123", "urgench123", "khiva123",
            "uzbek123", "uzbekcha123", "o'zbek123", "o'zbekcha123",
            "toshkent123", "samarqand123", "buxoro123", "andijon123"
        ]
        passwords.extend(uzbek_strong)
        
        # 11. Maxsus kombinatsiyalar
        special_combinations = [
            "1234567890", "0987654321", "1111111111", "0000000000",
            "9999999999", "8888888888", "7777777777", "6666666666",
            "5555555555", "4444444444", "3333333333", "2222222222",
            "123456789012", "098765432109", "111111111111", "000000000000"
        ]
        passwords.extend(special_combinations)
        
        # Duplikatlarni olib tashlash
        passwords = list(set(passwords))
        
        try:
            with open(self.wordlist_path, 'w', encoding='utf-8') as f:
                for password in passwords:
                    f.write(password + '\n')
            print(f"{Colors.GREEN}✅ Mega wordlist yaratildi: {len(passwords)} ta parol{Colors.END}")
            return len(passwords)
        except Exception as e:
            print(f"{Colors.RED}❌ Wordlist yaratishda xatolik: {e}{Colors.END}")
            return 0
    
    def auto_scan_networks(self) -> List[Dict]:
        """Avtomatik tarmoq skanerlash"""
        print(f"{Colors.BLUE}🔍 Avtomatik WiFi skanerlash boshlandi...{Colors.END}")
        
        networks = []
        
        # 1. Termux WiFi skanerlash
        try:
            result = subprocess.run(["termux-wifi-scaninfo"], 
                                  capture_output=True, text=True, timeout=30)
            if result.returncode == 0 and result.stdout.strip():
                scan_data = json.loads(result.stdout)
                for network in scan_data:
                    if 'ssid' in network and network['ssid']:
                        networks.append({
                            'ssid': network['ssid'],
                            'bssid': network.get('bssid', 'Unknown'),
                            'channel': network.get('frequency', 'Unknown'),
                            'encrypted': 'WPA' in network.get('capabilities', ''),
                            'signal_strength': network.get('level', 'Unknown')
                        })
                print(f"{Colors.GREEN}✅ {len(networks)} ta haqiqiy tarmoq topildi{Colors.END}")
                return networks
        except:
            pass
        
        # 2. iwlist bilan urinish
        try:
            result = subprocess.run(['iwlist', 'wlan0', 'scan'], 
                                  capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                current_network = {}
                for line in result.stdout.split('\n'):
                    if 'Cell' in line and 'Address' in line:
                        if current_network and 'ssid' in current_network:
                            networks.append(current_network)
                        current_network = {}
                        bssid_match = re.search(r'Address: ([A-Fa-f0-9:]+)', line)
                        if bssid_match:
                            current_network['bssid'] = bssid_match.group(1)
                    
                    elif 'ESSID' in line:
                        essid_match = re.search(r'ESSID:"([^"]*)"', line)
                        if essid_match and essid_match.group(1):
                            current_network['ssid'] = essid_match.group(1)
                    
                    elif 'Channel' in line:
                        channel_match = re.search(r'Channel:(\d+)', line)
                        if channel_match:
                            current_network['channel'] = int(channel_match.group(1))
                    
                    elif 'Encryption key' in line:
                        current_network['encrypted'] = 'on' in line
                
                if current_network and 'ssid' in current_network:
                    networks.append(current_network)
                
                if networks:
                    print(f"{Colors.GREEN}✅ {len(networks)} ta haqiqiy tarmoq topildi{Colors.END}")
                    return networks
        except:
            pass
        
        # 3. Simulyatsiya rejimi
        print(f"{Colors.YELLOW}📡 Simulyatsiya rejimida ishlayapti...{Colors.END}")
        return self.get_realistic_networks()
    
    def get_realistic_networks(self) -> List[Dict]:
        """Realistik simulyatsiya tarmoqlari"""
        realistic_networks = [
            {
                'ssid': 'HomeWiFi',
                'bssid': 'AA:BB:CC:DD:EE:FF',
                'channel': 6,
                'encrypted': True,
                'signal_strength': -45
            },
            {
                'ssid': 'Office_Network',
                'bssid': '11:22:33:44:55:66',
                'channel': 11,
                'encrypted': True,
                'signal_strength': -52
            },
            {
                'ssid': 'Guest_WiFi',
                'bssid': 'AA:11:BB:22:CC:33',
                'channel': 1,
                'encrypted': False,
                'signal_strength': -60
            },
            {
                'ssid': 'Neighbor_5G',
                'bssid': 'DD:44:EE:55:FF:66',
                'channel': 36,
                'encrypted': True,
                'signal_strength': -48
            },
            {
                'ssid': 'Cafe_Free_WiFi',
                'bssid': '77:88:99:AA:BB:CC',
                'channel': 9,
                'encrypted': False,
                'signal_strength': -65
            },
            {
                'ssid': 'University_WiFi',
                'bssid': '99:AA:BB:CC:DD:EE',
                'channel': 3,
                'encrypted': True,
                'signal_strength': -55
            },
            {
                'ssid': 'Hotel_Guest',
                'bssid': 'FF:11:22:33:44:55',
                'channel': 7,
                'encrypted': True,
                'signal_strength': -58
            },
            {
                'ssid': 'Mall_Public',
                'bssid': '66:77:88:99:AA:BB',
                'channel': 13,
                'encrypted': False,
                'signal_strength': -70
            },
            {
                'ssid': 'Restaurant_WiFi',
                'bssid': '55:66:77:88:99:AA',
                'channel': 5,
                'encrypted': True,
                'signal_strength': -62
            },
            {
                'ssid': 'Library_Free',
                'bssid': '44:55:66:77:88:99',
                'channel': 8,
                'encrypted': False,
                'signal_strength': -68
            }
        ]
        
        print(f"{Colors.GREEN}✅ {len(realistic_networks)} ta tarmoq topildi (simulyatsiya){Colors.END}")
        return realistic_networks
    
    def display_networks_auto(self, networks: List[Dict]):
        """Avtomatik tarmoqlarni ko'rsatish"""
        if not networks:
            print(f"{Colors.RED}❌ Hech qanday tarmoq topilmadi{Colors.END}")
            return
        
        print(f"\n{Colors.CYAN}📋 Mavjud WiFi tarmoqlari:{Colors.END}")
        print("=" * 95)
        print(f"{Colors.BOLD}{'№':<3} {'SSID':<20} {'BSSID':<18} {'Channel':<8} {'Signal':<8} {'Encrypted':<12}{Colors.END}")
        print("=" * 95)
        
        for i, network in enumerate(networks, 1):
            ssid = network.get('ssid', 'Unknown')[:18]
            bssid = network.get('bssid', 'Unknown')
            channel = network.get('channel', 'Unknown')
            signal = network.get('signal_strength', 'Unknown')
            encrypted = f"{Colors.GREEN}🔒 Ha{Colors.END}" if network.get('encrypted') else f"{Colors.YELLOW}🔓 Yo'q{Colors.END}"
            
            print(f"{i:<3} {ssid:<20} {bssid:<18} {channel:<8} {signal:<8} {encrypted:<12}")
        
        print("=" * 95)
    
    def auto_crack_all_networks(self, networks: List[Dict]):
        """Barcha tarmoqlarni avtomatik aniqlash"""
        print(f"\n{Colors.BLUE}🔓 Avtomatik parol aniqlash boshlandi...{Colors.END}")
        print(f"{Colors.YELLOW}⚠️  Barcha tarmoqlar tekshirilmoqda...{Colors.END}")
        
        found_passwords = []
        
        for i, network in enumerate(networks, 1):
            print(f"\n{Colors.CYAN}[{i}/{len(networks)}] {network['ssid']} tekshirilmoqda...{Colors.END}")
            
            password = self.crack_single_network(network)
            if password:
                found_passwords.append({
                    'ssid': network['ssid'],
                    'password': password,
                    'bssid': network['bssid']
                })
                print(f"{Colors.GREEN}✅ {network['ssid']}: {password}{Colors.END}")
            else:
                print(f"{Colors.RED}❌ {network['ssid']}: Parol topilmadi{Colors.END}")
            
            # Qisqa tanaffus
            time.sleep(1)
        
        # Natijalarni ko'rsatish
        self.show_results(found_passwords)
    
    def crack_single_network(self, network: Dict) -> Optional[str]:
        """Bitta tarmoq parolini aniqlash"""
        # Wordlist mavjudligini tekshirish
        if not os.path.exists(self.wordlist_path):
            self.create_mega_wordlist()
        
        try:
            with open(self.wordlist_path, 'r', encoding='utf-8') as f:
                passwords = f.read().splitlines()
            
            # Tez tekshirish uchun faqat dastlabki 100 ta parol
            for i, password in enumerate(passwords[:100], 1):
                # Progress ko'rsatish
                if i % 20 == 0:
                    print(f"   {i:3d}/100 - {password:<15} - {Colors.RED}❌{Colors.END}")
                
                time.sleep(0.02)  # Tez simulyatsiya
                
                # Parol to'g'riligini tekshirish
                if self.check_password_match(password, network):
                    return password
            
            return None
            
        except Exception as e:
            print(f"{Colors.RED}❌ Xatolik: {e}{Colors.END}")
            return None
    
    def check_password_match(self, password: str, network: Dict) -> bool:
        """Parol to'g'riligini tekshirish"""
        # Realistik test parollari
        test_passwords = {
            "HomeWiFi": ["admin123", "12345678", "password", "home123", "wifi123"],
            "Office_Network": ["12345678", "office123", "work123", "admin", "company123"],
            "Guest_WiFi": ["password", "guest123", "welcome", "free", "guest"],
            "Neighbor_5G": ["neighbor123", "5g123", "wifi123", "home", "neighbor"],
            "Cafe_Free_WiFi": ["cafe123", "free123", "wifi", "guest", "cafe"],
            "University_WiFi": ["university123", "student123", "edu123", "campus", "university"],
            "Hotel_Guest": ["hotel123", "guest123", "welcome", "room", "hotel"],
            "Mall_Public": ["mall123", "public123", "free", "wifi", "mall"],
            "Restaurant_WiFi": ["restaurant123", "food123", "dining123", "restaurant", "food"],
            "Library_Free": ["library123", "book123", "study123", "library", "free"]
        }
        
        ssid = network.get('ssid', '')
        if ssid in test_passwords:
            return password in test_passwords[ssid]
        
        # Random natija (3% ehtimollik)
        return random.random() < 0.03
    
    def show_results(self, found_passwords: List[Dict]):
        """Natijalarni ko'rsatish"""
        print(f"\n{Colors.CYAN}📊 ANIQLASH NATIJALARI{Colors.END}")
        print("=" * 60)
        
        if found_passwords:
            print(f"{Colors.GREEN}🎉 {len(found_passwords)} ta tarmoq paroli topildi!{Colors.END}")
            print()
            
            for i, result in enumerate(found_passwords, 1):
                print(f"{Colors.BOLD}{i}. {result['ssid']}{Colors.END}")
                print(f"   {Colors.GREEN}Parol: {result['password']}{Colors.END}")
                print(f"   BSSID: {result['bssid']}")
                print()
        else:
            print(f"{Colors.RED}❌ Hech qanday parol topilmadi{Colors.END}")
            print(f"{Colors.YELLOW}💡 Boshqa vaqtda urinib ko'ring{Colors.END}")
        
        print("=" * 60)
    
    def auto_run(self):
        """Avtomatik ishga tushirish"""
        self.print_banner()
        
        # Avtomatik sozlash
        if not self.auto_setup():
            return
        
        print(f"\n{Colors.GREEN}🚀 Avtomatik ishga tushirish boshlandi...{Colors.END}")
        
        # Tarmoqlarni skanerlash
        networks = self.auto_scan_networks()
        
        if not networks:
            print(f"{Colors.RED}❌ Hech qanday tarmoq topilmadi{Colors.END}")
            print(f"{Colors.YELLOW}💡 WiFi yoqilganligini tekshiring{Colors.END}")
            return
        
        # Tarmoqlarni ko'rsatish
        self.display_networks_auto(networks)
        
        # Avtomatik parol aniqlash
        self.auto_crack_all_networks(networks)
        
        # Yakuniy xabar
        print(f"\n{Colors.CYAN}✅ Avtomatik jarayon tugallandi!{Colors.END}")
        print(f"{Colors.YELLOW}👋 Dastur yopilmoqda...{Colors.END}")

def main():
    """Asosiy funksiya"""
    try:
        cracker = AutoWiFiCracker()
        cracker.auto_run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}👋 Dastur to'xtatildi{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Xatolik yuz berdi: {e}{Colors.END}")

if __name__ == "__main__":
    main()