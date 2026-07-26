# 🤖 JARVIS - AI Assistant Quick Start Guide

## ⚡ **FASTEST WAY TO ACCESS JARVIS (5 Minutes)**

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/attitudebmw007-lab/jarvis.git
cd jarvis
```

### **Step 2: Run Setup (Choose Your OS)**

**Windows Users:**
```bash
setup.bat
```

**Mac/Linux Users:**
```bash
bash setup.sh
```

Or **Manual Setup (All OS):**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

### **Step 3: Configure API Key**
```bash
# Copy environment file
cp .env.example .env

# Edit .env and add your OpenAI API key
# Get free key from: https://platform.openai.com/api-keys
```

### **Step 4: Launch JARVIS**

**Easiest Way - Interactive Menu:**
```bash
python launch.py
```

**Or Run Directly:**
```bash
# GUI Mode (Graphical Interface) - EASIEST
python gui/jarvis_gui.py

# Chat Mode (Type questions)
python main.py --chat

# Voice Mode (Speak commands)
python main.py --voice

# Combined Mode (Voice + Chat)
python main.py
```

---

## 🎯 **WHAT EACH MODE DOES**

| Mode | Command | How to Use |
|------|---------|-----------|
| **GUI** | `python gui/jarvis_gui.py` | ✅ **EASIEST** - Click buttons, type in window |
| **Chat** | `python main.py --chat` | Type your questions |
| **Voice** | `python main.py --voice` | Speak your commands |
| **Combined** | `python main.py` | Both voice and text |

---

## 🎤 **EXAMPLE COMMANDS TO TRY**

Once JARVIS is running, try:
```
"What's the time?"
"Tell me a joke"
"What's the weather?"
"Open notepad"
"Take a screenshot"
"System status"
"Hello"
"Help"
```

---

## 📦 **SYSTEM REQUIREMENTS**

- ✅ Python 3.8 or higher
- ✅ Microphone (for voice mode only)
- ✅ Internet connection
- ✅ OpenAI API key (free trial available)

---

## 🔑 **GET YOUR FREE API KEY IN 2 MINUTES**

1. Go to: https://platform.openai.com/api-keys
2. Sign up or log in
3. Click "Create new secret key"
4. Copy the key
5. Paste it in your `.env` file as: `OPENAI_API_KEY=sk-...`

---

## ⚙️ **DIFFERENT RESPONSE STYLES**

```bash
python main.py --style formal       # Professional
python main.py --style casual       # Friendly
python main.py --style technical    # Detailed
python main.py --style humorous     # Fun/Witty
```

---

## 🚨 **COMMON ISSUES & FIXES**

### **Error: "Module not found"**
```bash
pip install -r requirements.txt --upgrade
```

### **Error: "No microphone detected"**
```bash
pip install pyaudio
```

### **Error: "API key not valid"**
- Check your `.env` file has correct format
- Make sure key starts with `sk-`
- Verify at: https://platform.openai.com/account/api-keys

### **Error: "Permission denied" on Mac/Linux**
```bash
chmod +x setup.sh
bash setup.sh
```

---

## 📚 **DIRECTORY STRUCTURE**

```
jarvis/
├── main.py              # Main entry point
├── launch.py            # Easy launcher
├── setup.sh             # Mac/Linux setup
├── setup.bat            # Windows setup
├── .env.example         # Environment template
│
├── core/
│   ├── jarvis.py        # Main JARVIS class
│   ├── voice.py         # Voice recognition
│   └── nlp.py           # NLP processing
│
├── modules/
│   ├── ai_response.py   # OpenAI integration
│   ├── chat.py          # Chat interface
│   └── automation.py    # Task automation
│
├── gui/
│   └── jarvis_gui.py    # GUI Interface
│
└── data/
    ├── commands.json    # Commands
    └── responses.json   # Responses
```

---

## 🎮 **FEATURES YOU GET**

✅ **Voice Recognition** - Speak naturally  
✅ **Text-to-Speech** - Hear responses  
✅ **ChatGPT Integration** - AI answers  
✅ **Multiple Modes** - Voice, Chat, GUI  
✅ **Task Automation** - System commands  
✅ **Logging** - Track activities  
✅ **Multiple Styles** - Formal, Casual, Technical, Humorous  

---

## 📞 **NEED HELP?**

**Repository:** https://github.com/attitudebmw007-lab/jarvis

**Common Commands:**
```bash
python main.py --help           # Show all options
python main.py --chat --debug   # Chat with debug info
python main.py --voice --debug  # Voice with debug info
```

---

## 🎊 **YOU'RE ALL SET!**

Start with:
```bash
python launch.py
```

Then select option **1** for GUI (easiest) or **2** for Chat mode.

**Enjoy using JARVIS! 🤖✨**
