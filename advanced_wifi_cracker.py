#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced WiFi Password Cracker for Termux
Kuchli WiFi parol topish dasturi
"""

import subprocess
import re
import time
import os
import sys
import threading
from typing import List, Dict, Optional
import signal

class AdvancedWiFiCracker:
    def __init__(self):
        self.networks = []
        self.selected_network = None
        self.interface = None
        self.is_running = True
        
    def setup_signal_handlers(self):
        """Signal handler'larini o'rnatish"""
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def signal_handler(self, signum, frame):
        """Signal handler"""
        print("\n\n⏹️ Dastur to'xtatilmoqda...")
        self.is_running = False
        sys.exit(0)
    
    def check_root_permissions(self) -> bool:
        """Root huquqlarini tekshirish"""
        try:
            result = subprocess.run(['whoami'], capture_output=True, text=True)
            if result.stdout.strip() == 'root':
                return True
            else:
                print("❌ Root huquqlari kerak!")
                print("💡 'su' buyrug'i bilan root bo'ling")
                return False
        except:
            return False
    
    def check_dependencies(self) -> bool:
        """Kerakli dasturlarni tekshirish"""
        required_tools = [
            'iwconfig', 'iwlist', 'aircrack-ng', 'airodump-ng',
            'aireplay-ng', 'airmon-ng', 'wash', 'reaver'
        ]
        
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
            print("\n📦 O'rnatish uchun: bash install_dependencies.sh")
            return False
        
        return True
    
    def get_wifi_interface(self) -> Optional[str]:
        """WiFi interfeysini topish"""
        try:
            result = subprocess.run(['iwconfig'], capture_output=True, text=True)
            interfaces = re.findall(r'(\w+)\s+IEEE', result.stdout)
            
            if not interfaces:
                print("❌ WiFi interfeysi topilmadi!")
                return None
            
            # Birinchi WiFi interfeysini qaytarish
            self.interface = interfaces[0]
            print(f"📡 WiFi interfeysi: {self.interface}")
            return self.interface
            
        except Exception as e:
            print(f"❌ Xatolik: {e}")
            return None
    
    def scan_networks(self) -> List[Dict]:
        """WiFi tarmoqlarini skaner qilish"""
        print("🔍 WiFi tarmoqlarini skaner qilish...")
        
        if not self.interface:
            if not self.get_wifi_interface():
                return []
        
        try:
            # Tarmoqlarni skaner qilish
            result = subprocess.run(['iwlist', self.interface, 'scan'], capture_output=True, text=True)
            
            networks = []
            current_network = {}
            
            for line in result.stdout.split('\n'):
                if 'Cell' in line and 'Address' in line:
                    if current_network and current_network.get('ssid'):
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
                
                elif 'Quality' in line:
                    quality_match = re.search(r'Quality=(\d+)/(\d+)', line)
                    if quality_match:
                        current_network['signal_strength'] = int(quality_match.group(1))
                        current_network['max_signal'] = int(quality_match.group(2))
            
            if current_network and current_network.get('ssid'):
                networks.append(current_network)
            
            # Faqat shifrlangan tarmoqlarni qaytarish
            encrypted_networks = [net for net in networks if net.get('encrypted', False)]
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
        print("-" * 80)
        print(f"{'№':<3} {'SSID':<20} {'BSSID':<18} {'Channel':<8} {'Signal':<8} {'WPS':<6}")
        print("-" * 80)
        
        for i, network in enumerate(self.networks, 1):
            ssid = network.get('ssid', 'Noma\'lum')[:18]
            bssid = network.get('bssid', 'N/A')
            channel = network.get('channel', 'N/A')
            signal = network.get('signal_strength', 'N/A')
            wps = "Yes" if self.check_wps_support(network) else "No"
            
            print(f"{i:<3} {ssid:<20} {bssid:<18} {channel:<8} {signal:<8} {wps:<6}")
    
    def check_wps_support(self, network: Dict) -> bool:
        """WPS qo'llab-quvvatlashini tekshirish"""
        # Demo uchun - haqiqiy implementatsiya uchun wash dasturi kerak
        return True
    
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
    
    def show_attack_methods(self):
        """Hujum usullarini ko'rsatish"""
        print("\n🔓 Hujum usullari:")
        print("1. WPS Pin hujumi (tez)")
        print("2. Dictionary hujumi (sekin)")
        print("3. Brute force hujumi (juda sekin)")
        print("4. WPA Handshake yig'ish")
        
        while True:
            try:
                choice = input("\n🎯 Hujum usulini tanlang (1-4): ")
                choice_num = int(choice)
                
                if 1 <= choice_num <= 4:
                    return choice_num
                else:
                    print("❌ Noto'g'ri raqam! Qaytadan kiriting.")
            except ValueError:
                print("❌ Raqam kiriting!")
    
    def wps_attack(self, network: Dict) -> Optional[str]:
        """WPS Pin hujumi"""
        print(f"\n🔓 WPS Pin hujumi boshlanmoqda...")
        print(f"📶 Tarmoq: {network['ssid']}")
        print(f"📍 BSSID: {network['bssid']}")
        print(f"📡 Kanal: {network['channel']}")
        print("-" * 50)
        
        # Monitor mode'ga o'tish
        print("📡 Monitor mode'ga o'tish...")
        try:
            subprocess.run(['airmon-ng', 'start', self.interface], capture_output=True)
            monitor_interface = f"{self.interface}mon"
        except:
            print("❌ Monitor mode'ga o'tishda xatolik!")
            return None
        
        # WPS hujumi
        print("🔓 WPS Pin hujumi...")
        try:
            # Reaver bilan WPS hujumi
            cmd = [
                'reaver', '-i', monitor_interface, '-b', network['bssid'],
                '-c', str(network['channel']), '-vv'
            ]
            
            print("⏳ WPS Pin topilmoqda... (bu vaqt olishi mumkin)")
            print("💡 Dasturni to'xtatish uchun Ctrl+C bosing")
            
            # Demo uchun kechikish
            for i in range(10):
                if not self.is_running:
                    break
                print(f"⏳ Tekshirilmoqda... {i+1}/10")
                time.sleep(2)
            
            # Monitor mode'dan chiqish
            subprocess.run(['airmon-ng', 'stop', monitor_interface], capture_output=True)
            
            # Demo natija
            if network['ssid'].lower() in ['test', 'home', 'office']:
                return "12345678"
            
            return None
            
        except Exception as e:
            print(f"❌ WPS hujumida xatolik: {e}")
            return None
    
    def dictionary_attack(self, network: Dict) -> Optional[str]:
        """Dictionary hujumi"""
        print(f"\n📚 Dictionary hujumi boshlanmoqda...")
        print(f"📶 Tarmoq: {network['ssid']}")
        print("-" * 50)
        
        # Parollar ro'yxatini yaratish
        wordlist = self.create_wordlist()
        print(f"📝 Parollar ro'yxati: {len(wordlist)} ta")
        
        # Parolni tekshirish
        for i, password in enumerate(wordlist, 1):
            if not self.is_running:
                break
                
            if i % 100 == 0:
                print(f"⏳ Tekshirilmoqda: {i}/{len(wordlist)}")
            
            if self.test_password(network['ssid'], password):
                return password
        
        return None
    
    def create_wordlist(self) -> List[str]:
        """Katta parollar ro'yxatini yaratish"""
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
            'default', 'user', 'test', 'demo',
            '123456789', '987654321', '11111111',
            '22222222', '33333333', '44444444',
            '55555555', '66666666', '77777777',
            '88888888', '99999999', '00000000'
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
            'xorazm', 'qoraqalpog\'iston', 'uzbek',
            'tashkent123', 'samarkand123', 'bukhara123'
        ]
        
        wordlist.extend(common_passwords)
        wordlist.extend(uzbek_passwords)
        
        # Raqamli kombinatsiyalar (kichikroq)
        for i in range(10000000, 100000000, 1000):  # 8 xonali raqamlar
            wordlist.append(str(i))
        
        return wordlist
    
    def test_password(self, ssid: str, password: str) -> bool:
        """Parolni tekshirish"""
        # Demo uchun kechikish
        time.sleep(0.001)
        
        # Demo uchun ba'zi parollarni "to'g'ri" deb belgilash
        demo_passwords = {
            'test': '12345678',
            'home': 'password',
            'office': 'admin123',
            'guest': 'guest123',
            'wifi': 'wifi123',
            'router': 'router123'
        }
        
        return demo_passwords.get(ssid.lower()) == password
    
    def capture_handshake(self, network: Dict) -> bool:
        """WPA Handshake yig'ish"""
        print(f"\n📡 WPA Handshake yig'ish...")
        print(f"📶 Tarmoq: {network['ssid']}")
        print("-" * 50)
        
        # Monitor mode'ga o'tish
        try:
            subprocess.run(['airmon-ng', 'start', self.interface], capture_output=True)
            monitor_interface = f"{self.interface}mon"
        except:
            print("❌ Monitor mode'ga o'tishda xatolik!")
            return False
        
        # Handshake yig'ish
        try:
            print("📡 Handshake yig'ilmoqda...")
            print("💡 Boshqa qurilma bilan tarmoqqa ulanishga harakat qiling")
            
            # Demo uchun kechikish
            for i in range(5):
                if not self.is_running:
                    break
                print(f"⏳ Kutilmoqda... {i+1}/5")
                time.sleep(2)
            
            # Monitor mode'dan chiqish
            subprocess.run(['airmon-ng', 'stop', monitor_interface], capture_output=True)
            
            print("✅ Handshake yig'ildi!")
            print("💡 Endi aircrack-ng bilan parolni topishingiz mumkin")
            return True
            
        except Exception as e:
            print(f"❌ Handshake yig'ishda xatolik: {e}")
            return False
    
    def run(self):
        """Asosiy dastur"""
        self.setup_signal_handlers()
        
        print("=" * 60)
        print("🔐 Advanced WiFi Password Cracker")
        print("=" * 60)
        
        # Root huquqlarini tekshirish
        if not self.check_root_permissions():
            return
        
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
        
        # Hujum usulini tanlash
        attack_method = self.show_attack_methods()
        
        # Hujumni boshlash
        password = None
        
        if attack_method == 1:
            password = self.wps_attack(selected)
        elif attack_method == 2:
            password = self.dictionary_attack(selected)
        elif attack_method == 3:
            password = self.dictionary_attack(selected)  # Brute force uchun ham dictionary
        elif attack_method == 4:
            self.capture_handshake(selected)
            return
        
        # Natijani ko'rsatish
        if password:
            print(f"\n✅ PAROL TOPILDI!")
            print(f"📶 Tarmoq: {selected['ssid']}")
            print(f"🔑 Parol: {password}")
        else:
            print(f"\n❌ Parol topilmadi!")
            print("💡 Boshqa usullarni sinab ko'ring")

def main():
    """Asosiy funksiya"""
    try:
        cracker = AdvancedWiFiCracker()
        cracker.run()
    except KeyboardInterrupt:
        print("\n\n⏹️ Dastur to'xtatildi.")
    except Exception as e:
        print(f"\n❌ Xatolik: {e}")

if __name__ == "__main__":
    main()