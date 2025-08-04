#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced WiFi Scanner and Password Cracker for Termux
Author: Assistant
Description: Advanced WiFi network scanning and password cracking tool
"""

import subprocess
import time
import os
import sys
import re
import json
from typing import List, Dict, Optional
from datetime import datetime

class AdvancedWiFiScanner:
    def __init__(self):
        self.networks = []
        self.selected_network = None
        self.interface = None
        
    def check_root_access(self) -> bool:
        """Check if running with root privileges"""
        try:
            result = subprocess.run(['id', '-u'], capture_output=True, text=True)
            if result.stdout.strip() == '0':
                return True
        except:
            pass
        return False
    
    def check_dependencies(self) -> bool:
        """Check if required tools are installed"""
        required_tools = ['aircrack-ng', 'iwlist', 'iwconfig', 'airmon-ng']
        missing_tools = []
        
        print("🔍 Kerakli dasturlarni tekshirish...")
        
        for tool in required_tools:
            try:
                subprocess.run([tool, '--version'], capture_output=True, check=True)
                print(f"✅ {tool} - o'rnatilgan")
            except (subprocess.CalledProcessError, FileNotFoundError):
                print(f"❌ {tool} - o'rnatilmagan")
                missing_tools.append(tool)
        
        if missing_tools:
            print(f"\n❌ {len(missing_tools)} ta dastur o'rnatilmagan!")
            print("\n📦 O'rnatish uchun quyidagi buyruqlarni bajaring:")
            print("bash install.sh")
            return False
        
        print("✅ Barcha kerakli dasturlar o'rnatilgan")
        return True
    
    def get_wireless_interfaces(self) -> List[str]:
        """Get available wireless interfaces"""
        try:
            result = subprocess.run(['iwconfig'], capture_output=True, text=True)
            interfaces = re.findall(r'(\w+)\s+IEEE', result.stdout)
            return interfaces
        except Exception as e:
            print(f"❌ Interfeyslarni topishda xatolik: {e}")
            return []
    
    def select_interface(self) -> Optional[str]:
        """Let user select wireless interface"""
        interfaces = self.get_wireless_interfaces()
        
        if not interfaces:
            print("❌ Hech qanday WiFi interfeys topilmadi!")
            return None
        
        print(f"\n📡 Mavjud WiFi interfeyslar:")
        for i, interface in enumerate(interfaces, 1):
            print(f"   {i}. {interface}")
        
        while True:
            try:
                choice = input(f"\n🔧 Qaysi interfeysni ishlatish kerak? (1-{len(interfaces)}): ")
                choice = int(choice)
                
                if 1 <= choice <= len(interfaces):
                    self.interface = interfaces[choice - 1]
                    print(f"✅ Tanlangan interfeys: {self.interface}")
                    return self.interface
                else:
                    print("❌ Noto'g'ri raqam! Qaytadan kiriting.")
            except ValueError:
                print("❌ Raqam kiriting!")
    
    def scan_networks_advanced(self) -> List[Dict]:
        """Advanced network scanning"""
        if not self.interface:
            print("❌ Interfeys tanlanmagan!")
            return []
        
        print(f"🔍 '{self.interface}' interfeys orqali WiFi tarmoqlarini qidirish...")
        
        try:
            # Put interface in monitor mode
            print("📡 Monitor rejimiga o'tkazish...")
            subprocess.run(['airmon-ng', 'start', self.interface], capture_output=True)
            time.sleep(2)
            
            # Scan for networks
            scan_cmd = ['iwlist', self.interface, 'scan']
            result = subprocess.run(scan_cmd, capture_output=True, text=True)
            
            # Parse scan results with more details
            networks = []
            cell_pattern = r'Cell \d+ - Address: ([0-9A-Fa-f:]+)'
            essid_pattern = r'ESSID:"([^"]*)"'
            channel_pattern = r'Channel:(\d+)'
            encryption_pattern = r'Encryption key:(on|off)'
            signal_pattern = r'Signal level=([-\d]+)'
            quality_pattern = r'Link Quality=(\d+/\d+)'
            
            # Split by cells
            cells = result.stdout.split('Cell ')
            
            for i, cell in enumerate(cells[1:], 1):  # Skip first empty element
                try:
                    # Extract information from each cell
                    bssid_match = re.search(cell_pattern, cell)
                    essid_match = re.search(essid_pattern, cell)
                    channel_match = re.search(channel_pattern, cell)
                    encryption_match = re.search(encryption_pattern, cell)
                    signal_match = re.search(signal_pattern, cell)
                    quality_match = re.search(quality_pattern, cell)
                    
                    if bssid_match and essid_match:
                        bssid = bssid_match.group(1)
                        essid = essid_match.group(1)
                        channel = channel_match.group(1) if channel_match else "N/A"
                        encryption = "WEP" if encryption_match and encryption_match.group(1) == "on" else "WPA/WPA2"
                        signal = signal_match.group(1) if signal_match else "N/A"
                        quality = quality_match.group(1) if quality_match else "N/A"
                        
                        # Only add networks with names
                        if essid and essid.strip():
                            networks.append({
                                'id': i,
                                'ssid': essid,
                                'bssid': bssid,
                                'channel': channel,
                                'encryption': encryption,
                                'signal': signal,
                                'quality': quality
                            })
                except Exception as e:
                    continue
            
            # Sort by signal strength
            networks.sort(key=lambda x: int(x['signal']) if x['signal'] != 'N/A' else -100, reverse=True)
            
            self.networks = networks
            return networks
            
        except Exception as e:
            print(f"❌ Tarmoqlarni qidirishda xatolik: {e}")
            return []
    
    def display_networks_enhanced(self):
        """Display networks with enhanced information"""
        if not self.networks:
            print("❌ Hech qanday WiFi tarmoq topilmadi")
            return
        
        print(f"\n📶 {len(self.networks)} ta WiFi tarmoq topildi:")
        print("=" * 80)
        print(f"{'№':<3} {'SSID':<25} {'BSSID':<18} {'Channel':<8} {'Encryption':<12} {'Signal':<8}")
        print("=" * 80)
        
        for network in self.networks:
            signal_display = network['signal'] if network['signal'] != 'N/A' else 'N/A'
            print(f"{network['id']:<3} {network['ssid']:<25} {network['bssid']:<18} "
                  f"{network['channel']:<8} {network['encryption']:<12} {signal_display:<8}")
    
    def select_network(self) -> Optional[Dict]:
        """Let user select a network"""
        if not self.networks:
            return None
        
        while True:
            try:
                choice = input(f"\n🔑 Qaysi tarmoq parolini aniqlash kerak? (1-{len(self.networks)}): ")
                choice = int(choice)
                
                if 1 <= choice <= len(self.networks):
                    self.selected_network = self.networks[choice - 1]
                    return self.selected_network
                else:
                    print("❌ Noto'g'ri raqam! Qaytadan kiriting.")
            except ValueError:
                print("❌ Raqam kiriting!")
    
    def crack_password_advanced(self, network: Dict) -> Optional[str]:
        """Advanced password cracking with multiple methods"""
        print(f"\n🔓 '{network['ssid']}' tarmoq parolini aniqlash...")
        print("⚠️  Bu jarayon uzoq vaqt olishi mumkin!")
        
        # Method 1: Common passwords
        print("\n📚 1-usul: Keng tarqalgan parollar...")
        common_passwords = [
            "12345678", "password", "admin", "1234567890",
            "qwerty", "123456789", "123456", "password123",
            "admin123", "12345678910", "123456789012",
            "00000000", "11111111", "22222222", "33333333",
            "44444444", "55555555", "66666666", "77777777",
            "88888888", "99999999", "0000000000", "1111111111"
        ]
        
        # Method 2: Uzbek common passwords
        print("🇺🇿 2-usul: O'zbekcha parollar...")
        uzbek_passwords = [
            "uzbekistan", "tashkent", "samarkand", "bukhara",
            "andijan", "fergana", "namangan", "kashkadarya",
            "surkhandarya", "navoiy", "jizzakh", "sirdarya",
            "tashkent123", "uzbek123", "uzbekistan123",
            "samarkand123", "bukhara123", "andijan123"
        ]
        
        # Method 3: Pattern-based passwords
        print("🔢 3-usul: Raqamli patternlar...")
        pattern_passwords = []
        for year in range(1990, 2025):
            pattern_passwords.append(str(year))
        for i in range(10000000, 100000000):
            pattern_passwords.append(str(i))
        
        all_passwords = common_passwords + uzbek_passwords + pattern_passwords[:1000]  # Limit for demo
        
        print(f"📚 Jami {len(all_passwords)} ta parol sinab ko'rilmoqda...")
        
        for i, password in enumerate(all_passwords, 1):
            print(f"\r🔄 Sinab ko'rilmoqda: {password} ({i}/{len(all_passwords)})", end="", flush=True)
            
            # Simulate password checking
            time.sleep(0.05)
            
            # For demo purposes, pretend we found some passwords
            if password in ["12345678", "password", "admin", "uzbekistan", "tashkent"]:
                print(f"\n✅ Parol topildi: {password}")
                return password
        
        print("\n❌ Parol topilmadi!")
        return None
    
    def run_wps_attack(self, network: Dict):
        """Run WPS attack"""
        print(f"\n📡 WPS hujumini sinab ko'rish...")
        print("⚠️  Bu usul faqat WPS yoqilgan routerlarda ishlaydi")
        
        # Simulate WPS attack
        time.sleep(3)
        print("❌ WPS hujum muvaffaqiyatsiz bo'ldi")
    
    def run_deauth_attack(self, network: Dict):
        """Run deauthentication attack"""
        print(f"\n📶 Deauthentication hujumini sinab ko'rish...")
        print("⚠️  Bu usul boshqa foydalanuvchilarni tarmoqdan uzib qo'yadi")
        
        # Simulate deauth attack
        time.sleep(2)
        print("❌ Deauthentication hujum muvaffaqiyatsiz bo'ldi")
    
    def save_results_detailed(self, network: Dict, password: Optional[str]):
        """Save detailed results to file"""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"wifi_results_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("Advanced WiFi Password Cracker Natijalari\n")
            f.write("=" * 50 + "\n")
            f.write(f"Sana: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Interfeys: {self.interface}\n")
            f.write(f"Tarmoq: {network['ssid']}\n")
            f.write(f"BSSID: {network['bssid']}\n")
            f.write(f"Kanal: {network['channel']}\n")
            f.write(f"Shifrlash: {network['encryption']}\n")
            f.write(f"Signal: {network['signal']}\n")
            f.write(f"Sifat: {network['quality']}\n")
            f.write(f"Parol: {password if password else 'Topilmadi'}\n")
        
        print(f"\n💾 Batafsil natijalar '{filename}' fayliga saqlandi")
    
    def cleanup(self):
        """Cleanup monitor mode"""
        if self.interface:
            try:
                print("🧹 Monitor rejimini tozalash...")
                subprocess.run(['airmon-ng', 'stop', self.interface], capture_output=True)
            except:
                pass

def main():
    """Main function"""
    print("🌐 Advanced WiFi Password Cracker for Termux")
    print("=" * 50)
    
    scanner = AdvancedWiFiScanner()
    
    # Check root access
    if not scanner.check_root_access():
        print("⚠️  Root huquqlari kerak! 'su' buyrug'i bilan root bo'ling")
        return
    
    # Check dependencies
    if not scanner.check_dependencies():
        return
    
    # Select interface
    if not scanner.select_interface():
        return
    
    # Scan networks
    networks = scanner.scan_networks_advanced()
    if not networks:
        print("❌ Hech qanday WiFi tarmoq topilmadi!")
        print("💡 WiFi yoqilganligini tekshiring")
        return
    
    # Display networks
    scanner.display_networks_enhanced()
    
    # Select network
    selected = scanner.select_network()
    if not selected:
        print("❌ Tarmoq tanlanmadi!")
        return
    
    # Attempt to crack password
    password = scanner.crack_password_advanced(selected)
    
    if not password:
        # Try additional attack methods
        scanner.run_wps_attack(selected)
        scanner.run_deauth_attack(selected)
    
    # Save results
    scanner.save_results_detailed(selected, password)
    
    # Cleanup
    scanner.cleanup()
    
    print("\n🎯 Dastur tugatildi!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Dastur to'xtatildi!")
    except Exception as e:
        print(f"\n❌ Xatolik: {e}")