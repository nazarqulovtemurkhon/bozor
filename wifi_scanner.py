#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WiFi Scanner for Termux
Author: Assistant
Description: Scan WiFi networks and attempt to connect
"""

import subprocess
import re
import time
import os
import sys
from typing import List, Dict, Optional

class WiFiScanner:
    def __init__(self):
        self.networks = []
        self.selected_network = None
        
    def check_dependencies(self) -> bool:
        """Check if required tools are installed"""
        print("🔍 Dasturlarni tekshirish...")
        
        # Check if we're in Termux
        if not os.path.exists('/data/data/com.termux'):
            print("❌ Bu dastur faqat Termux da ishlaydi!")
            return False
        
        # Check for basic tools
        try:
            subprocess.run(['termux-wifi-scaninfo'], capture_output=True, check=True)
            print("✅ termux-wifi-scaninfo mavjud")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ termux-wifi-scaninfo topilmadi!")
            print("📦 O'rnatish: pkg install termux-api")
            return False
        
        return True
    
    def scan_networks(self) -> List[Dict]:
        """Scan for available WiFi networks using Termux API"""
        print("🔍 WiFi tarmoqlarini skanerlayapman...")
        
        try:
            # Use termux-wifi-scaninfo to get network information
            result = subprocess.run(['termux-wifi-scaninfo'], capture_output=True, text=True)
            
            if result.returncode != 0:
                print("❌ WiFi skanerlashda xatolik!")
                return []
            
            # Parse JSON-like output
            networks = []
            lines = result.stdout.strip().split('\n')
            
            current_network = {}
            for line in lines:
                line = line.strip()
                
                if 'SSID:' in line:
                    if current_network:
                        networks.append(current_network)
                    current_network = {}
                    ssid_match = re.search(r'SSID:\s*"([^"]*)"', line)
                    if ssid_match:
                        current_network['ssid'] = ssid_match.group(1)
                
                elif 'BSSID:' in line:
                    bssid_match = re.search(r'BSSID:\s*([0-9A-Fa-f:]+)', line)
                    if bssid_match:
                        current_network['bssid'] = bssid_match.group(1)
                
                elif 'RSSI:' in line:
                    rssi_match = re.search(r'RSSI:\s*(-?\d+)', line)
                    if rssi_match:
                        current_network['rssi'] = int(rssi_match.group(1))
                
                elif 'capabilities:' in line:
                    if 'WPA' in line or 'WEP' in line:
                        current_network['encrypted'] = True
                    else:
                        current_network['encrypted'] = False
            
            if current_network:
                networks.append(current_network)
            
            # Filter out networks without SSID
            networks = [net for net in networks if net.get('ssid')]
            
            return networks
            
        except Exception as e:
            print(f"❌ Tarmoqlarni skanerlashda xatolik: {e}")
            return []
    
    def display_networks(self, networks: List[Dict]):
        """Display available networks in a numbered list"""
        if not networks:
            print("❌ Hech qanday WiFi tarmog'i topilmadi!")
            return
        
        print(f"\n📡 Topilgan WiFi tarmoqlari ({len(networks)} ta):")
        print("=" * 60)
        
        for i, network in enumerate(networks, 1):
            ssid = network.get('ssid', 'Noma\'lum')
            bssid = network.get('bssid', 'N/A')
            rssi = network.get('rssi', 'N/A')
            encrypted = "🔒" if network.get('encrypted', False) else "🔓"
            
            # Signal strength indicator
            if isinstance(rssi, int):
                if rssi >= -50:
                    signal = "📶📶📶"
                elif rssi >= -70:
                    signal = "📶📶"
                else:
                    signal = "📶"
            else:
                signal = "❓"
            
            print(f"{i:2d}. {encrypted} {ssid}")
            print(f"    MAC: {bssid} | Signal: {signal} ({rssi} dBm)")
            print()
        
        self.networks = networks
    
    def select_network(self) -> Optional[Dict]:
        """Let user select a network to connect to"""
        if not self.networks:
            print("❌ Skanerlash natijalari mavjud emas!")
            return None
        
        while True:
            try:
                choice = input(f"🎯 Ulanish uchun tarmoq raqamini kiriting (1-{len(self.networks)}): ")
                choice = int(choice)
                
                if 1 <= choice <= len(self.networks):
                    selected = self.networks[choice - 1]
                    print(f"\n✅ Tanlangan tarmoq: {selected['ssid']}")
                    return selected
                else:
                    print("❌ Noto'g'ri raqam! Qaytadan kiriting.")
            except ValueError:
                print("❌ Raqam kiriting!")
            except KeyboardInterrupt:
                print("\n\n👋 Dastur to'xtatildi.")
                sys.exit(0)
    
    def attempt_connection(self, network: Dict):
        """Attempt to connect to the selected network"""
        ssid = network['ssid']
        print(f"🔗 {ssid} ga ulanishga harakat qilish...")
        
        # Try common passwords
        common_passwords = [
            "",  # Open network
            "12345678",
            "password",
            "1234567890",
            "qwerty123",
            "admin123",
            "123456789",
            "password123",
            "12345678910",
            "admin",
            "root",
            "user",
            "guest",
            "welcome",
            "123456",
            "1234567",
            "qwerty",
            "abc123"
        ]
        
        print("🔍 Oddiy parollarni sinab ko'rish...")
        
        for i, password in enumerate(common_passwords, 1):
            print(f"   {i:2d}. Parolni sinab ko'rish: {'(ochiq tarmoq)' if password == '' else password}")
            
            try:
                # Use termux-wifi-connectinfo to attempt connection
                if password:
                    cmd = ['termux-wifi-connectinfo', '-s', ssid, '-p', password]
                else:
                    cmd = ['termux-wifi-connectinfo', '-s', ssid]
                
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
                
                if result.returncode == 0:
                    print(f"\n🎉 MUVOFIQQIYATLI ULANDI!")
                    print(f"📶 Tarmoq: {ssid}")
                    if password:
                        print(f"🔑 Parol: {password}")
                    else:
                        print(f"🔓 Ochiq tarmoq (parol yo'q)")
                    return True
                
            except subprocess.TimeoutExpired:
                print("   ⏰ Vaqt tugadi")
            except Exception as e:
                print(f"   ❌ Xatolik: {e}")
        
        print(f"\n❌ {ssid} ga ulanishda muvaffaqiyatsizlik!")
        print("💡 Boshqa parollarni sinab ko'ring yoki tarmoq egasidan so'rang.")
        return False
    
    def run(self):
        """Main execution method"""
        print("📡 WiFi Scanner")
        print("=" * 30)
        
        # Check dependencies
        if not self.check_dependencies():
            return
        
        try:
            # Scan networks
            networks = self.scan_networks()
            self.display_networks(networks)
            
            # Select target network
            target = self.select_network()
            if not target:
                return
            
            # Attempt connection
            self.attempt_connection(target)
                
        except KeyboardInterrupt:
            print("\n\n👋 Dastur to'xtatildi.")
        except Exception as e:
            print(f"\n❌ Kutilmagan xatolik: {e}")

def main():
    """Main function"""
    scanner = WiFiScanner()
    scanner.run()

if __name__ == "__main__":
    main()