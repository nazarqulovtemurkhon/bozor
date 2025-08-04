#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple WiFi Test Script
Tests basic WiFi scanning functionality
"""

import subprocess
import os
import sys

def test_termux_environment():
    """Test if we're running in Termux"""
    print("🔍 Termux muhitini tekshirish...")
    
    if os.path.exists('/data/data/com.termux'):
        print("✅ Termux muhitida ishlayapmiz")
        return True
    else:
        print("❌ Bu Termux muhiti emas!")
        return False

def test_python():
    """Test Python installation"""
    print("🐍 Python versiyasini tekshirish...")
    
    try:
        version = sys.version_info
        print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    except Exception as e:
        print(f"❌ Python xatoligi: {e}")
        return False

def test_termux_api():
    """Test Termux API availability"""
    print("📱 Termux API ni tekshirish...")
    
    try:
        result = subprocess.run(['termux-wifi-scaninfo'], 
                              capture_output=True, text=True, timeout=5)
        
        if result.returncode == 0:
            print("✅ Termux API mavjud")
            return True
        else:
            print("❌ Termux API xatoligi")
            print(f"Xatolik: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("❌ termux-wifi-scaninfo topilmadi!")
        print("📦 O'rnatish: pkg install termux-api")
        return False
    except subprocess.TimeoutExpired:
        print("❌ Termux API vaqt tugadi")
        return False
    except Exception as e:
        print(f"❌ Termux API xatoligi: {e}")
        return False

def test_wifi_scan():
    """Test basic WiFi scanning"""
    print("📡 WiFi skanerlashni sinab ko'rish...")
    
    try:
        result = subprocess.run(['termux-wifi-scaninfo'], 
                              capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            output = result.stdout.strip()
            if output:
                print("✅ WiFi skanerlash muvaffaqiyatli!")
                print(f"📊 Natija uzunligi: {len(output)} belgi")
                
                # Count networks
                network_count = output.count('SSID:')
                print(f"📶 Topilgan tarmoqlar: {network_count} ta")
                
                return True
            else:
                print("⚠️ WiFi skanerlash natijasi bo'sh")
                return False
        else:
            print("❌ WiFi skanerlashda xatolik")
            print(f"Xatolik: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ WiFi skanerlash xatoligi: {e}")
        return False

def main():
    """Main test function"""
    print("🧪 WiFi Scanner Test")
    print("=" * 30)
    
    tests = [
        ("Termux muhiti", test_termux_environment),
        ("Python", test_python),
        ("Termux API", test_termux_api),
        ("WiFi skanerlash", test_wifi_scan)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 {test_name}...")
        if test_func():
            passed += 1
        print()
    
    print("=" * 30)
    print(f"📊 Natija: {passed}/{total} test muvaffaqiyatli")
    
    if passed == total:
        print("🎉 Barcha testlar muvaffaqiyatli!")
        print("✅ WiFi Scanner ishlatishga tayyor!")
    else:
        print("❌ Ba'zi testlar muvaffaqiyatsiz!")
        print("📖 README.md faylini o'qing va kerakli dasturlarni o'rnating")
    
    return passed == total

if __name__ == "__main__":
    main()