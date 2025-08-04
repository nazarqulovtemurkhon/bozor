#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
from typing import List, Dict

class DemoWiFiScanner:
    def __init__(self):
        # Demo networks for testing
        self.demo_networks = [
            {'essid': 'MegaLine_WiFi', 'mac': '00:11:22:33:44:55', 'quality': '45/70', 'encryption': 'WPA2'},
            {'essid': 'UzbekTelecom_5G', 'mac': '66:77:88:99:AA:BB', 'quality': '38/70', 'encryption': 'WPA2'},
            {'essid': 'AndroidAP', 'mac': 'CC:DD:EE:FF:00:11', 'quality': '52/70', 'encryption': 'WPA'},
            {'essid': 'Guest_Network', 'mac': '22:33:44:55:66:77', 'quality': '28/70', 'encryption': 'Open'},
            {'essid': 'admin', 'mac': '88:99:AA:BB:CC:DD', 'quality': '55/70', 'encryption': 'WPA2'},
            {'essid': 'password123', 'mac': 'EE:FF:00:11:22:33', 'quality': '33/70', 'encryption': 'WPA'},
        ]
        self.networks = []
        
    def scan_networks(self):
        """Demo WiFi network scan"""
        print("🔍 WiFi tarmoqlarini qidiryapman...")
        
        # Simulate scanning delay
        for i in range(3):
            print(f"{'.' * (i+1)}")
            time.sleep(0.5)
        
        # Return demo networks
        self.networks = self.demo_networks
        print(f"✅ {len(self.networks)} ta tarmoq topildi!")
        return self.networks
    
    def display_networks(self):
        """Display found networks with numbering"""
        if not self.networks:
            print("❌ Hech qanday WiFi tarmoq topilmadi")
            return
        
        print("\n📡 Topilgan WiFi tarmoqlari:")
        print("-" * 60)
        print(f"{'#':<3} {'Nom':<25} {'Signal':<10} {'Shifrlash':<10}")
        print("-" * 60)
        
        for i, network in enumerate(self.networks, 1):
            print(f"{i:<3} {network['essid']:<25} {network['quality']:<10} {network['encryption']:<10}")
        
        print("-" * 60)
    
    def dictionary_attack(self, network_name: str) -> str:
        """Demo password attack"""
        print(f"\n🔐 {network_name} uchun parol qidiryapman...")
        
        # Common passwords list
        common_passwords = [
            "password", "123456789", "12345678", "admin", "password123",
            "qwerty", "letmein", "welcome", "monkey", "dragon",
            "password1", "123456", "1234567890", "internet", "service"
        ]
        
        # Add network name variations
        name_variations = [
            network_name.lower(),
            network_name.upper(),
            network_name + "123",
            network_name + "321",
            network_name + "password"
        ]
        
        all_passwords = common_passwords + name_variations
        
        print(f"📝 {len(all_passwords)} ta parol sinab ko'ryapman...")
        
        for i, password in enumerate(all_passwords, 1):
            print(f"⏳ Sinab ko'rish {i}/{len(all_passwords)}: {password}")
            
            # Simulate testing delay
            time.sleep(0.2)
            
            # Demo success condition
            if self._demo_test_password(network_name, password):
                print(f"✅ Parol topildi: {password}")
                return password
        
        print("❌ Parol topilmadi")
        return None
    
    def _demo_test_password(self, network_name: str, password: str) -> bool:
        """Demo password testing"""
        # Simulate some passwords working
        success_conditions = [
            network_name.lower() == password,
            network_name + "123" == password,
            password == "admin" and network_name == "admin",
            password == "password123" and network_name == "password123",
            password == "password" and "guest" in network_name.lower()
        ]
        
        return any(success_conditions)
    
    def show_demo_saved_passwords(self):
        """Show demo saved passwords"""
        print("\n🔑 Demo saqlangan parollar:")
        demo_saved = {
            "MyHome_WiFi": "myhome123",
            "Office_Network": "office2023",
            "Neighbors_WiFi": "neighbor456"
        }
        
        print("-" * 50)
        for ssid, password in demo_saved.items():
            print(f"📡 {ssid}: {password}")
        print("-" * 50)
    
    def main_menu(self):
        """Main demo menu"""
        print("🌐 WiFi Parol Aniqlash Dasturi (DEMO)")
        print("=" * 45)
        print("⚠️  Bu demo versiya - haqiqiy WiFi skanermaydi")
        print("")
        
        while True:
            print("\n📋 Menyu:")
            print("1. WiFi tarmoqlarini qidirish (Demo)")
            print("2. Saqlangan parollarni ko'rish (Demo)")
            print("3. Haqiqiy dastur haqida ma'lumot")
            print("4. Chiqish")
            
            choice = input("\nTanlang (1-4): ").strip()
            
            if choice == '1':
                self.demo_scan_and_crack()
            elif choice == '2':
                self.show_demo_saved_passwords()
            elif choice == '3':
                self.show_real_info()
            elif choice == '4':
                print("👋 Demo tugadi")
                break
            else:
                print("❌ Noto'g'ri tanlov")
    
    def demo_scan_and_crack(self):
        """Demo scan and crack process"""
        networks = self.scan_networks()
        if not networks:
            return
        
        self.display_networks()
        
        try:
            choice = int(input("\nQaysi WiFi tarmoqni tanlaysiz? (raqam kiriting): "))
            if 1 <= choice <= len(networks):
                selected_network = networks[choice - 1]
                print(f"\n📶 Tanlandi: {selected_network['essid']}")
                print(f"🔒 Shifrlash: {selected_network['encryption']}")
                
                if selected_network['encryption'] == 'Open':
                    print("✅ Bu tarmoq ochiq (parolsiz)")
                else:
                    password = self.dictionary_attack(selected_network['essid'])
                    if password:
                        print(f"\n🎉 Demo muvaffaqiyatli! Parol: {password}")
                        print("💡 Haqiqiy dasturda bu parol ishlatib ulanish mumkin")
                    else:
                        print("\n💡 Demo: Parol topilmadi")
            else:
                print("❌ Noto'g'ri raqam")
        except ValueError:
            print("❌ Iltimos, raqam kiriting")
    
    def show_real_info(self):
        """Show information about real usage"""
        print("\n" + "="*50)
        print("📖 HAQIQIY DASTUR HAQIDA MA'LUMOT")
        print("="*50)
        print("\n🔧 Haqiqiy dasturni ishlatish uchun:")
        print("1. Termux-da root ruxsati oling:")
        print("   pkg install tsu")
        print("   tsu")
        print("")
        print("2. Kerakli dasturlarni o'rnating:")
        print("   ./setup.sh")
        print("")
        print("3. Haqiqiy dasturni ishga tushiring:")
        print("   python3 wifi_scanner.py")
        print("")
        print("⚠️  MUHIM OGOHLANTIRISHLAR:")
        print("• Faqat o'zingizga tegishli WiFi sinang")
        print("• Bu faqat ta'lim maqsadida")
        print("• Noqonuniy foydalanish taqiqlanadi")
        print("")
        print("🛡️  XAVFSIZLIK:")
        print("• Root ruxsati xavfli bo'lishi mumkin")
        print("• Faqat ishonchli tarmoqlarga ulaning")
        print("• Shaxsiy ma'lumotlaringizni himoya qiling")
        print("="*50)

def main():
    try:
        demo_scanner = DemoWiFiScanner()
        demo_scanner.main_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Demo to'xtatildi")
    except Exception as e:
        print(f"\n❌ Kutilmagan xatolik: {e}")

if __name__ == "__main__":
    main()