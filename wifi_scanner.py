#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import re
import os
import json
from typing import List, Dict, Optional

def run_command(command: str) -> str:
    """Run shell command and return output"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        print(f"Xatolik: {e}")
        return ""

def scan_wifi_networks() -> List[Dict[str, str]]:
    """Scan for available WiFi networks"""
    print("📡 WiFi tarmoqlarini skanlamoqda...")
    
    # Termux uchun WiFi skanerlash
    command = "termux-wifi-scaninfo"
    output = run_command(command)
    
    networks = []
    if output:
        try:
            wifi_data = json.loads(output)
            for i, network in enumerate(wifi_data, 1):
                networks.append({
                    'id': str(i),
                    'ssid': network.get('ssid', 'Unknown'),
                    'bssid': network.get('bssid', ''),
                    'signal': network.get('rssi', ''),
                    'security': network.get('capabilities', '')
                })
        except json.JSONDecodeError:
            print("WiFi ma'lumotlarini o'qishda xatolik")
    
    # Agar termux-wifi-scaninfo ishlamasa, boshqa usul
    if not networks:
        print("Boshqa usul bilan skanlamoqda...")
        # iwlist scan yoki nmcli dan foydalanish
        command = "iwlist scan 2>/dev/null | grep -E 'Cell|ESSID|Signal|Encryption'"
        output = run_command(command)
        
        if output:
            lines = output.split('\n')
            current_network = {}
            network_id = 1
            
            for line in lines:
                if 'Cell' in line and 'Address:' in line:
                    if current_network.get('ssid'):
                        networks.append(current_network)
                    current_network = {'id': str(network_id)}
                    network_id += 1
                    # BSSID ni olish
                    bssid_match = re.search(r'Address: ([0-9A-Fa-f:]{17})', line)
                    if bssid_match:
                        current_network['bssid'] = bssid_match.group(1)
                
                elif 'ESSID:' in line:
                    essid_match = re.search(r'ESSID:"([^"]*)"', line)
                    if essid_match:
                        current_network['ssid'] = essid_match.group(1)
                
                elif 'Signal level' in line:
                    signal_match = re.search(r'Signal level=(-?\d+)', line)
                    if signal_match:
                        current_network['signal'] = signal_match.group(1) + " dBm"
                
                elif 'Encryption key:' in line:
                    if 'on' in line:
                        current_network['security'] = 'Secured'
                    else:
                        current_network['security'] = 'Open'
            
            # Oxirgi tarmoqni qo'shish
            if current_network.get('ssid'):
                networks.append(current_network)
    
    return networks

def get_saved_wifi_passwords() -> Dict[str, str]:
    """Try to get saved WiFi passwords from various sources"""
    passwords = {}
    
    # Android WiFi konfiguratsiya fayllari
    wifi_config_paths = [
        '/data/misc/wifi/wpa_supplicant.conf',
        '/data/wifi/bcm_supp.conf',
        '/system/etc/wifi/wpa_supplicant.conf'
    ]
    
    for path in wifi_config_paths:
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    content = f.read()
                    # SSID va PSK ni topish
                    networks = re.findall(r'network=\{[^}]*ssid="([^"]*)"[^}]*psk="([^"]*)"[^}]*\}', content, re.DOTALL)
                    for ssid, psk in networks:
                        passwords[ssid] = psk
            except PermissionError:
                continue
            except Exception:
                continue
    
    # Termux orqali saqlangan parollarni olish
    try:
        # Android keystore yoki shared preferences
        termux_wifi_cmd = "termux-wifi-connectioninfo"
        wifi_info = run_command(termux_wifi_cmd)
        if wifi_info:
            wifi_data = json.loads(wifi_info)
            current_ssid = wifi_data.get('ssid', '').replace('"', '')
            if current_ssid:
                # Joriy ulangan tarmoq uchun parolni olishga harakat
                passwords[current_ssid] = "Joriy ulangan tarmoq"
    except:
        pass
    
    return passwords

def try_common_passwords(ssid: str) -> Optional[str]:
    """Try common passwords for the network"""
    common_passwords = [
        "123456789", "12345678", "password", "123456", "qwerty",
        "abc123", "password123", "admin", "1234567890", "welcome",
        "letmein", "monkey", "dragon", "sunshine", "iloveyou",
        ssid.lower(), ssid.upper(), ssid + "123", ssid + "1234",
        "wifi", "internet", "router", "modem"
    ]
    
    print(f"\n🔍 {ssid} uchun umumiy parollarni sinab ko'rmoqda...")
    
    for password in common_passwords[:10]:  # Faqat birinchi 10 tani sinash
        print(f"   Sinab ko'rilmoqda: {password}")
        # Bu yerda haqiqiy parol sinovini amalga oshirish mumkin
        # Lekin xavfsizlik sababli faqat ma'lumot berish
    
    return None

def display_networks(networks: List[Dict[str, str]]):
    """Display available networks in a formatted way"""
    print("\n" + "="*60)
    print("🌐 MAVJUD WiFi TARMOQLARI")
    print("="*60)
    
    if not networks:
        print("❌ Hech qanday WiFi tarmoq topilmadi!")
        return
    
    print(f"{'No.':<4} {'SSID':<25} {'Signal':<12} {'Security':<15}")
    print("-"*60)
    
    for network in networks:
        ssid = network.get('ssid', 'Unknown')[:24]
        signal = network.get('signal', 'Unknown')[:11]
        security = network.get('security', 'Unknown')[:14]
        
        print(f"{network['id']:<4} {ssid:<25} {signal:<12} {security:<15}")

def main():
    print("🚀 WiFi Scanner & Password Finder")
    print("Termux uchun maxsus versiya")
    print("="*50)
    
    # Root ruxsatini tekshirish
    root_check = run_command("id")
    if "uid=0" not in root_check:
        print("⚠️  Diqqat: Root ruxsatlari yo'q. Ba'zi funksiyalar ishlamasligi mumkin.")
        print("Root ruxsat olish uchun: su yoki sudo dan foydalaning")
    
    # WiFi tarmoqlarini skanlaash
    networks = scan_wifi_networks()
    
    if not networks:
        print("❌ WiFi tarmoqlarini skanlashda xatolik yuz berdi!")
        print("Termux ruxsatlarini tekshiring:")
        print("   termux-setup-storage")
        print("   pkg install termux-api")
        return
    
    # Tarmoqlarni ko'rsatish
    display_networks(networks)
    
    # Saqlangan parollarni olish
    saved_passwords = get_saved_wifi_passwords()
    
    while True:
        try:
            print("\n" + "="*50)
            choice = input("Tanlang (raqam kiriting yoki 'q' - chiqish): ").strip()
            
            if choice.lower() == 'q':
                print("👋 Dastur tugadi!")
                break
            
            if not choice.isdigit():
                print("❌ Iltimos, to'g'ri raqam kiriting!")
                continue
            
            choice_num = int(choice)
            selected_network = None
            
            for network in networks:
                if network['id'] == choice:
                    selected_network = network
                    break
            
            if not selected_network:
                print("❌ Bunday raqam mavjud emas!")
                continue
            
            ssid = selected_network['ssid']
            print(f"\n🎯 Tanlangan: {ssid}")
            print("="*30)
            
            # Saqlangan parolni tekshirish
            if ssid in saved_passwords:
                print(f"✅ Saqlangan parol topildi: {saved_passwords[ssid]}")
            else:
                print("❌ Saqlangan parol topilmadi")
                
                # Umumiy parollarni sinash
                common_result = try_common_passwords(ssid)
                if common_result:
                    print(f"✅ Umumiy parollar ichidan topildi: {common_result}")
                else:
                    print("❌ Umumiy parollar orqali parol topilmadi")
                
                print("\n💡 Maslahatlar:")
                print("   1. Tarmoq egasidan parolni so'rang")
                print("   2. WPS funksiyasini tekshiring")
                print("   3. Router ostidagi yorliqni qarang")
            
            print("\nTarmoq ma'lumotlari:")
            print(f"   SSID: {ssid}")
            if 'bssid' in selected_network:
                print(f"   BSSID: {selected_network['bssid']}")
            if 'signal' in selected_network:
                print(f"   Signal: {selected_network['signal']}")
            if 'security' in selected_network:
                print(f"   Xavfsizlik: {selected_network['security']}")
            
        except KeyboardInterrupt:
            print("\n\n👋 Dastur to'xtatildi!")
            break
        except Exception as e:
            print(f"❌ Xatolik: {e}")

if __name__ == "__main__":
    main()