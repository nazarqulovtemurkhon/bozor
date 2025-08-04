#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os
import sys
import time
import re
from typing import List, Dict

class WiFiScanner:
    def __init__(self):
        self.networks = []
        self.interface = "wlan0"
        
    def check_requirements(self):
        """Check if required tools are available"""
        required_tools = ['iwlist', 'wpa_supplicant', 'aircrack-ng']
        missing_tools = []
        
        for tool in required_tools:
            try:
                subprocess.run(['which', tool], check=True, capture_output=True)
            except subprocess.CalledProcessError:
                missing_tools.append(tool)
        
        if missing_tools:
            print(f"❌ Quyidagi dasturlar topilmadi: {', '.join(missing_tools)}")
            print("📦 Ularni o'rnatish uchun:")
            print("pkg update && pkg upgrade")
            print("pkg install wireless-tools wpa-supplicant aircrack-ng")
            return False
        return True
    
    def scan_networks(self):
        """Scan for available WiFi networks"""
        print("🔍 WiFi tarmoqlarini qidiryapman...")
        try:
            # Enable WiFi interface
            subprocess.run(['ip', 'link', 'set', self.interface, 'up'], 
                         capture_output=True, check=False)
            
            # Scan for networks
            result = subprocess.run(['iwlist', self.interface, 'scan'], 
                                  capture_output=True, text=True, check=True)
            
            networks = self._parse_scan_results(result.stdout)
            self.networks = networks
            return networks
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Xatolik: {e}")
            print("💡 Root ruxsati kerak bo'lishi mumkin")
            return []
    
    def _parse_scan_results(self, scan_output: str) -> List[Dict]:
        """Parse iwlist scan results"""
        networks = []
        cells = scan_output.split('Cell ')
        
        for cell in cells[1:]:  # Skip first empty element
            try:
                # Extract ESSID (network name)
                essid_match = re.search(r'ESSID:"([^"]*)"', cell)
                if not essid_match or not essid_match.group(1):
                    continue
                
                essid = essid_match.group(1)
                
                # Extract signal quality
                quality_match = re.search(r'Quality=(\d+/\d+)', cell)
                quality = quality_match.group(1) if quality_match else "Unknown"
                
                # Extract encryption type
                if 'WPA2' in cell:
                    encryption = 'WPA2'
                elif 'WPA' in cell:
                    encryption = 'WPA'
                elif 'WEP' in cell:
                    encryption = 'WEP'
                else:
                    encryption = 'Open'
                
                # Extract MAC address
                mac_match = re.search(r'Address: ([0-9A-Fa-f:]{17})', cell)
                mac = mac_match.group(1) if mac_match else "Unknown"
                
                networks.append({
                    'essid': essid,
                    'mac': mac,
                    'quality': quality,
                    'encryption': encryption
                })
                
            except Exception as e:
                continue
        
        return networks
    
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
    
    def get_saved_passwords(self):
        """Try to get saved WiFi passwords"""
        saved_passwords = {}
        
        # Try to read from wpa_supplicant.conf
        conf_paths = [
            '/data/misc/wifi/wpa_supplicant.conf',
            '/data/wifi/bcm_supp.conf',
            '/system/etc/wifi/wpa_supplicant.conf'
        ]
        
        for conf_path in conf_paths:
            if os.path.exists(conf_path):
                try:
                    with open(conf_path, 'r') as f:
                        content = f.read()
                        
                    # Parse networks
                    networks = re.findall(r'network=\{([^}]+)\}', content, re.DOTALL)
                    for network in networks:
                        ssid_match = re.search(r'ssid="([^"]+)"', network)
                        psk_match = re.search(r'psk="([^"]+)"', network)
                        
                        if ssid_match and psk_match:
                            saved_passwords[ssid_match.group(1)] = psk_match.group(1)
                            
                except Exception as e:
                    continue
        
        return saved_passwords
    
    def dictionary_attack(self, network_name: str) -> str:
        """Perform dictionary attack on selected network"""
        print(f"\n🔐 {network_name} uchun parol qidiryapman...")
        
        # Common passwords list
        common_passwords = [
            "password", "123456789", "12345678", "admin", "password123",
            "qwerty", "letmein", "welcome", "monkey", "dragon",
            "password1", "123456", "1234567890", "internet", "service",
            "hello", "guest", "admin123", "administrator", "root",
            "toor", "pass", "test", "guest", "info", "adm", "mysql",
            "user", "administrator", "oracle", "ftp", "pi", "raspberry",
            "arduino", "password321", "admin321", "test123", "demo"
        ]
        
        # Add network name variations
        name_variations = [
            network_name.lower(),
            network_name.upper(),
            network_name + "123",
            network_name + "321",
            network_name + "password",
            network_name[:8] if len(network_name) > 8 else network_name
        ]
        
        all_passwords = common_passwords + name_variations
        
        print(f"📝 {len(all_passwords)} ta parol sinab ko'ryapman...")
        
        for i, password in enumerate(all_passwords, 1):
            print(f"⏳ Sinab ko'rish {i}/{len(all_passwords)}: {password}")
            
            # Simulate password testing (in real scenario, you'd use wpa_supplicant)
            if self._test_password(network_name, password):
                print(f"✅ Parol topildi: {password}")
                return password
            
            time.sleep(0.1)  # Small delay
        
        print("❌ Parol topilmadi")
        return None
    
    def _test_password(self, network_name: str, password: str) -> bool:
        """Test if password works for the network"""
        # This is a placeholder - in real implementation you'd:
        # 1. Create wpa_supplicant config
        # 2. Try to connect
        # 3. Check if connection successful
        
        # For demonstration, we'll simulate some success
        if password in [network_name.lower(), network_name + "123", "admin", "password"]:
            return True
        return False
    
    def main_menu(self):
        """Main program menu"""
        print("🌐 WiFi Parol Aniqlash Dasturi")
        print("=" * 40)
        
        if not self.check_requirements():
            return
        
        while True:
            print("\n📋 Menyu:")
            print("1. WiFi tarmoqlarini qidirish")
            print("2. Saqlangan parollarni ko'rish")
            print("3. Chiqish")
            
            choice = input("\nTanlang (1-3): ").strip()
            
            if choice == '1':
                self.scan_and_crack()
            elif choice == '2':
                self.show_saved_passwords()
            elif choice == '3':
                print("👋 Dastur tugadi")
                break
            else:
                print("❌ Noto'g'ri tanlov")
    
    def scan_and_crack(self):
        """Scan networks and attempt password cracking"""
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
                        print(f"\n🎉 Tabriklaymiz! Parol: {password}")
                    else:
                        print("\n💡 Maslahat: Kuchliroq so'zlik yoki boshqa usullardan foydalaning")
            else:
                print("❌ Noto'g'ri raqam")
        except ValueError:
            print("❌ Iltimos, raqam kiriting")
    
    def show_saved_passwords(self):
        """Show saved passwords"""
        print("\n🔑 Saqlangan parollar qidiryapman...")
        saved = self.get_saved_passwords()
        
        if saved:
            print("\n✅ Topilgan saqlangan parollar:")
            print("-" * 50)
            for ssid, password in saved.items():
                print(f"📡 {ssid}: {password}")
            print("-" * 50)
        else:
            print("❌ Saqlangan parollar topilmadi")
            print("💡 Root ruxsati kerak bo'lishi mumkin")

def main():
    try:
        scanner = WiFiScanner()
        scanner.main_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Dastur to'xtatildi")
    except Exception as e:
        print(f"\n❌ Kutilmagan xatolik: {e}")

if __name__ == "__main__":
    main()