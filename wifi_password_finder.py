#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WiFi Password Finder for Termux
Bu dastur WiFi tarmoqlarini skaner qiladi va parollarni topishga harakat qiladi
"""

import subprocess
import re
import time
import os
import sys
from typing import List, Dict, Optional

class WiFiPasswordFinder:
    def __init__(self):
        self.networks = []
        self.selected_network = None
        
    def check_dependencies(self) -> bool:
        """Kerakli dasturlar mavjudligini tekshirish"""
        required_tools = ['iwlist', 'aircrack-ng', 'airodump-ng']
        missing_tools = []
        
        for tool in required_tools:
            try:
                subprocess.run([tool, '--help'], capture_output=True, check=True)
            except (subprocess.CalledProcessError, FileNotFoundError):
                missing_tools.append(tool)
        
        if missing_tools:
            print("❌ Quyidagi dasturlar o'rnatilmagan:")
            for tool in missing_tools:
                print(f"   - {tool}")
            print("\n📦 O'rnatish uchun quyidagi buyruqlarni ishga tushiring:")
            print("pkg update && pkg upgrade")
            print("pkg install aircrack-ng")
            return False
        
        return True
    
    def scan_networks(self) -> List[Dict]:
        """WiFi tarmoqlarini skaner qilish"""
        print("🔍 WiFi tarmoqlarini skaner qilish...")
        
        try:
            # WiFi interfeysini topish
            result = subprocess.run(['iwconfig'], capture_output=True, text=True)
            interfaces = re.findall(r'(\w+)\s+IEEE', result.stdout)
            
            if not interfaces:
                print("❌ WiFi interfeysi topilmadi!")
                return []
            
            interface = interfaces[0]
            print(f"📡 Interfeys: {interface}")
            
            # Tarmoqlarni skaner qilish
            result = subprocess.run(['iwlist', interface, 'scan'], capture_output=True, text=True)
            
            networks = []
            current_network = {}
            
            for line in result.stdout.split('\n'):
                if 'Cell' in line and 'Address' in line:
                    if current_network:
                        networks.append(current_network)
                    current_network = {}
                    current_network['bssid'] = re.search(r'Address: ([A-Fa-f0-9:]+)', line).group(1)
                
                elif 'ESSID' in line:
                    essid_match = re.search(r'ESSID:"([^"]*)"', line)
                    if essid_match:
                        current_network['ssid'] = essid_match.group(1)
                
                elif 'Channel' in line:
                    channel_match = re.search(r'Channel:(\d+)', line)
                    if channel_match:
                        current_network['channel'] = int(channel_match.group(1))
                
                elif 'Encryption key:on' in line:
                    current_network['encrypted'] = True
                elif 'Encryption key:off' in line:
                    current_network['encrypted'] = False
            
            if current_network:
                networks.append(current_network)
            
            # Faqat shifrlangan tarmoqlarni qaytarish
            encrypted_networks = [net for net in networks if net.get('encrypted', False) and net.get('ssid')]
            self.networks = encrypted_networks
            
            return encrypted_networks
            
        except Exception as e:
            print(f"❌ Xatolik: {e}")
            return []
    
    def display_networks(self):
        """Tarmoqlar ro'yxatini ko'rsatish"""
        if not self.networks:
            print("❌ Hech qanday WiFi tarmoq topilmadi!")
            return
        
        print("\n📶 Topilgan WiFi tarmoqlar:")
        print("-" * 60)
        print(f"{'№':<3} {'SSID':<20} {'BSSID':<18} {'Channel':<8}")
        print("-" * 60)
        
        for i, network in enumerate(self.networks, 1):
            ssid = network.get('ssid', 'Noma\'lum')[:18]
            bssid = network.get('bssid', 'N/A')
            channel = network.get('channel', 'N/A')
            print(f"{i:<3} {ssid:<20} {bssid:<18} {channel:<8}")
    
    def select_network(self) -> Optional[Dict]:
        """Tarmoq tanlash"""
        if not self.networks:
            return None
        
        while True:
            try:
                choice = input(f"\n🎯 Tarmoq tanlang (1-{len(self.networks)}): ")
                choice_num = int(choice)
                
                if 1 <= choice_num <= len(self.networks):
                    self.selected_network = self.networks[choice_num - 1]
                    return self.selected_network
                else:
                    print("❌ Noto'g'ri raqam! Qaytadan kiriting.")
            except ValueError:
                print("❌ Raqam kiriting!")
    
    def create_wordlist(self):
        """Oddiy parollar ro'yxatini yaratish"""
        wordlist = []
        
        # Oddiy parollar
        common_passwords = [
            '12345678', 'password', 'admin', '1234567890',
            'qwerty', '123456789', '123456', 'password123',
            'admin123', '12345678910', '123456789012',
            '00000000', '11111111', '22222222', '33333333',
            '44444444', '55555555', '66666666', '77777777',
            '88888888', '99999999', '0000000000',
            '0123456789', '9876543210', '123123123',
            'qwertyuiop', 'asdfghjkl', 'zxcvbnm',
            'qwerty123', 'password1', 'admin1',
            '123456789a', 'password123', 'admin123',
            'wifi', 'internet', 'network', 'router',
            'modem', 'home', 'office', 'guest',
            'default', 'user', 'test', 'demo'
        ]
        
        # Uzbecha parollar
        uzbek_passwords = [
            'uzbekistan', 'tashkent', 'samarkand', 'bukhara',
            'andijan', 'fergana', 'namangan', 'kashkadarya',
            'surkhandarya', 'navoiy', 'jizzakh', 'sirdarya',
            'khorezm', 'karakalpakstan', 'qoraqalpogiston',
            'o\'zbekiston', 'toshkent', 'samarqand', 'buxoro',
            'andijon', 'farg\'ona', 'namangan', 'qashqadaryo',
            'surxondaryo', 'navoiy', 'jizzax', 'sirdaryo',
            'xorazm', 'qoraqalpog\'iston'
        ]
        
        wordlist.extend(common_passwords)
        wordlist.extend(uzbek_passwords)
        
        # Raqamli kombinatsiyalar
        for i in range(10000000, 100000000):  # 8 xonali raqamlar
            wordlist.append(str(i))
        
        return wordlist
    
    def crack_password(self, network: Dict) -> Optional[str]:
        """Parolni topishga harakat qilish"""
        ssid = network.get('ssid')
        bssid = network.get('bssid')
        channel = network.get('channel')
        
        print(f"\n🔓 Parol topish jarayoni boshlanmoqda...")
        print(f"📶 Tarmoq: {ssid}")
        print(f"📍 BSSID: {bssid}")
        print(f"📡 Kanal: {channel}")
        print("-" * 50)
        
        # Parollar ro'yxatini yaratish
        wordlist = self.create_wordlist()
        print(f"📝 Parollar ro'yxati: {len(wordlist)} ta")
        
        # Parolni tekshirish
        for i, password in enumerate(wordlist, 1):
            if i % 1000 == 0:
                print(f"⏳ Tekshirilmoqda: {i}/{len(wordlist)}")
            
            # Bu yerda haqiqiy parol tekshirish logikasi bo'lishi kerak
            # Hozircha demo uchun oddiy tekshirish
            if self.test_password(ssid, password):
                return password
        
        return None
    
    def test_password(self, ssid: str, password: str) -> bool:
        """Parolni tekshirish (demo versiya)"""
        # Bu demo versiya - haqiqiy implementatsiya uchun
        # aircrack-ng yoki boshqa vositalar kerak
        time.sleep(0.001)  # Demo uchun kechikish
        
        # Demo uchun ba'zi parollarni "to'g'ri" deb belgilash
        demo_passwords = {
            'test': '12345678',
            'home': 'password',
            'office': 'admin123',
            'guest': 'guest123'
        }
        
        return demo_passwords.get(ssid.lower()) == password
    
    def run(self):
        """Asosiy dastur"""
        print("=" * 60)
        print("🔐 WiFi Password Finder - Termux uchun")
        print("=" * 60)
        
        # Dasturlarni tekshirish
        if not self.check_dependencies():
            return
        
        # Tarmoqlarni skaner qilish
        networks = self.scan_networks()
        if not networks:
            print("❌ Hech qanday WiFi tarmoq topilmadi!")
            return
        
        # Tarmoqlarni ko'rsatish
        self.display_networks()
        
        # Tarmoq tanlash
        selected = self.select_network()
        if not selected:
            print("❌ Tarmoq tanlanmadi!")
            return
        
        # Parolni topish
        password = self.crack_password(selected)
        
        if password:
            print(f"\n✅ PAROL TOPILDI!")
            print(f"📶 Tarmoq: {selected['ssid']}")
            print(f"🔑 Parol: {password}")
        else:
            print(f"\n❌ Parol topilmadi!")
            print("💡 Boshqa usullarni sinab ko'ring yoki")
            print("   boshqa tarmoqni tanlang.")

def main():
    """Asosiy funksiya"""
    try:
        finder = WiFiPasswordFinder()
        finder.run()
    except KeyboardInterrupt:
        print("\n\n⏹️ Dastur to'xtatildi.")
    except Exception as e:
        print(f"\n❌ Xatolik: {e}")

if __name__ == "__main__":
    main()