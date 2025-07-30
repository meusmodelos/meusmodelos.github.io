#!/usr/bin/env python3
"""
Backend Test for Sitefy HTML Editor Application
Tests the static HTML files and their functionality
"""

import requests
import sys
from datetime import datetime
import re
from bs4 import BeautifulSoup

class SitefyHTMLTester:
    def __init__(self, base_url="http://localhost:8080"):
        self.base_url = base_url
        self.tests_run = 0
        self.tests_passed = 0

    def run_test(self, name, test_func):
        """Run a single test"""
        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        
        try:
            success = test_func()
            if success:
                self.tests_passed += 1
                print(f"✅ Passed")
            else:
                print(f"❌ Failed")
            return success
        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            return False

    def test_home_page_loads(self):
        """Test if home.html loads successfully"""
        response = requests.get(f"{self.base_url}/home.html", timeout=10)
        return response.status_code == 200 and len(response.text) > 1000

    def test_editor_page_loads(self):
        """Test if editor.html loads successfully"""
        response = requests.get(f"{self.base_url}/editor.html", timeout=10)
        return response.status_code == 200 and len(response.text) > 1000

    def test_home_page_structure(self):
        """Test home.html structure and content"""
        response = requests.get(f"{self.base_url}/home.html", timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check for Sitefy logo
        logo = soup.find('h1')
        if not logo or 'Sitefy' not in logo.text:
            print("❌ Sitefy logo not found")
            return False
        
        # Check for black/red theme (CSS)
        style_content = str(soup.find('style'))
        if '#000000' not in style_content or '#dc143c' not in style_content:
            print("❌ Black/red theme colors not found in CSS")
            return False
        
        # Check for welcome section
        welcome = soup.find(class_='welcome-section')
        if not welcome:
            print("❌ Welcome section not found")
            return False
        
        # Check for "Modelos Prontos" section
        modelos_section = soup.find(id='modelosProntos')
        if not modelos_section:
            print("❌ Modelos Prontos section not found")
            return False
        
        # Check for "Modelo Desenho Vetorial" card
        modelo_card = soup.find(text='Modelo Desenho Vetorial')
        if not modelo_card:
            print("❌ Modelo Desenho Vetorial card not found")
            return False
        
        print("✅ All structural elements found")
        return True

    def test_usar_modelo_function(self):
        """Test if usarModelo function exists in JavaScript"""
        response = requests.get(f"{self.base_url}/home.html", timeout=10)
        
        # Check if usarModelo function is defined
        if 'function usarModelo(' not in response.text:
            print("❌ usarModelo function not found")
            return False
        
        # Check if the function has the expected structure
        if 'modelosProntos[modeloId]' not in response.text:
            print("❌ usarModelo function doesn't access modelosProntos")
            return False
        
        print("✅ usarModelo function found and properly structured")
        return True

    def test_complex_html_model(self):
        """Test if the complex HTML model (Pica-pau) exists"""
        response = requests.get(f"{self.base_url}/home.html", timeout=10)
        
        # Check for Pica-pau model content
        if 'Pica-Pau Vetorial' not in response.text:
            print("❌ Pica-pau model title not found")
            return False
        
        # Check for complex CSS animations
        if '@keyframes' not in response.text:
            print("❌ CSS animations not found")
            return False
        
        # Check for woody class (main character element)
        if 'class="woody"' not in response.text:
            print("❌ Woody character class not found")
            return False
        
        # Check for animation properties
        if 'animation:' not in response.text:
            print("❌ Animation properties not found")
            return False
        
        print("✅ Complex HTML model with animations found")
        return True

    def test_editor_page_structure(self):
        """Test editor.html structure"""
        response = requests.get(f"{self.base_url}/editor.html", timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check for canvas element
        canvas = soup.find(id='canvas')
        if not canvas:
            print("❌ Canvas element not found")
            return False
        
        # Check for mobile frame reference
        if '375x667' not in response.text:
            print("❌ Mobile viewport reference not found")
            return False
        
        # Check for complex HTML loading functions
        if 'isComplexHTML' not in response.text:
            print("❌ isComplexHTML function not found")
            return False
        
        if 'loadComplexHTML' not in response.text:
            print("❌ loadComplexHTML function not found")
            return False
        
        print("✅ Editor structure and functions found")
        return True

    def test_mobile_responsiveness(self):
        """Test mobile responsiveness indicators"""
        response = requests.get(f"{self.base_url}/home.html", timeout=10)
        
        # Check for viewport meta tag
        if 'viewport' not in response.text or 'width=device-width' not in response.text:
            print("❌ Mobile viewport meta tag not found")
            return False
        
        # Check for mobile-specific CSS
        if '@media' not in response.text:
            print("❌ Media queries for responsiveness not found")
            return False
        
        # Check for max-width constraints
        if 'max-width: 375px' not in response.text:
            print("❌ Mobile width constraints not found")
            return False
        
        print("✅ Mobile responsiveness features found")
        return True

    def test_firebase_integration(self):
        """Test Firebase integration setup"""
        response = requests.get(f"{self.base_url}/home.html", timeout=10)
        
        # Check for Firebase scripts
        if 'firebase-app-compat.js' not in response.text:
            print("❌ Firebase app script not found")
            return False
        
        if 'firebase-auth-compat.js' not in response.text:
            print("❌ Firebase auth script not found")
            return False
        
        # Check for Firebase config
        if 'firebaseConfig' not in response.text:
            print("❌ Firebase configuration not found")
            return False
        
        print("✅ Firebase integration setup found")
        return True

def main():
    print("🚀 Starting Sitefy HTML Editor Tests")
    print("=" * 50)
    
    tester = SitefyHTMLTester()
    
    # Run all tests
    tests = [
        ("Home Page Loading", tester.test_home_page_loads),
        ("Editor Page Loading", tester.test_editor_page_loads),
        ("Home Page Structure", tester.test_home_page_structure),
        ("usarModelo Function", tester.test_usar_modelo_function),
        ("Complex HTML Model (Pica-pau)", tester.test_complex_html_model),
        ("Editor Page Structure", tester.test_editor_page_structure),
        ("Mobile Responsiveness", tester.test_mobile_responsiveness),
        ("Firebase Integration", tester.test_firebase_integration),
    ]
    
    for test_name, test_func in tests:
        tester.run_test(test_name, test_func)
    
    # Print results
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {tester.tests_passed}/{tester.tests_run} tests passed")
    
    if tester.tests_passed == tester.tests_run:
        print("🎉 All tests passed! The Sitefy HTML editor is working correctly.")
        return 0
    else:
        print(f"⚠️  {tester.tests_run - tester.tests_passed} tests failed. Please review the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())