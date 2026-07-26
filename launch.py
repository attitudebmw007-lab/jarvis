"""Easy launcher script for JARVIS - Quick Start Guide."""

import os
import sys
import subprocess
import platform

def print_header():
    """Print welcome header."""
    print("\n" + "="*70)
    print("  🤖 JARVIS - AI ASSISTANT LAUNCHER")
    print("="*70 + "\n")

def check_requirements():
    """Check if all requirements are installed."""
    print("📋 Checking requirements...")
    try:
        import openai
        import speech_recognition
        import pyttsx3
        print("✅ All requirements installed!\n")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {str(e)}")
        print("Run: pip install -r requirements.txt\n")
        return False

def check_env_file():
    """Check if .env file exists and has API key."""
    print("🔑 Checking API configuration...")
    if not os.path.exists('.env'):
        print("⚠️  .env file not found!")
        print("Creating .env from .env.example...\n")
        if os.path.exists('.env.example'):
            with open('.env.example', 'r') as f:
                content = f.read()
            with open('.env', 'w') as f:
                f.write(content)
            print("📝 Please edit .env and add your OpenAI API key")
            print("Get your key from: https://platform.openai.com/api-keys\n")
            return False
    
    with open('.env', 'r') as f:
        content = f.read()
        if 'sk-' not in content or 'your-api-key' in content.lower():
            print("❌ OpenAI API key not found in .env")
            print("Edit .env and add your API key\n")
            return False
    
    print("✅ API key configured!\n")
    return True

def show_menu():
    """Show launch menu."""
    print("Choose how to run JARVIS:\n")
    print("1️⃣  GUI Mode (Graphical Interface)")
    print("2️⃣  Chat Mode (Text-based)")
    print("3️⃣  Voice Mode (Voice Commands)")
    print("4️⃣  Combined Mode (Voice + Chat)")
    print("5️⃣  Formal Style (Professional)")
    print("6️⃣  Humorous Style (Fun)")
    print("7️⃣  Technical Style (Detailed)")
    print("8️⃣  Exit\n")

def run_jarvis(mode):
    """Run JARVIS with selected mode."""
    commands = {
        '1': 'python gui/jarvis_gui.py',
        '2': 'python main.py --chat',
        '3': 'python main.py --voice',
        '4': 'python main.py',
        '5': 'python main.py --style formal',
        '6': 'python main.py --style humorous',
        '7': 'python main.py --style technical'
    }
    
    if mode in commands:
        print(f"\n🚀 Launching JARVIS...\n")
        os.system(commands[mode])
    else:
        print("❌ Invalid option!")

def main():
    """Main launcher function."""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print_header()
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Check environment setup
    if not check_env_file():
        response = input("Continue anyway? (y/n): ").lower()
        if response != 'y':
            print("❌ Setup incomplete. Please configure .env first.")
            sys.exit(1)
    
    # Show menu and get choice
    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == '8':
            print("\n👋 Thank you for using JARVIS!\n")
            sys.exit(0)
        
        run_jarvis(choice)
        
        print("\n" + "="*70)
        print("  Press Enter to return to menu...")
        input()
        print("\n" * 2)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 JARVIS launcher terminated.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)
