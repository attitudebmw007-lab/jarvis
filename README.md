# JARVIS - AI Assistant

A Python-based AI assistant inspired by Iron Man's JARVIS. Features voice recognition, chat interface, task automation, and intelligent AI responses.

## Features

✅ **Voice Recognition** - Speak commands naturally  
✅ **Chat Interface** - Text-based conversations  
✅ **Task Automation** - Execute automated tasks  
✅ **AI Responses** - Intelligent, context-aware answers  
✅ **Natural Language Processing** - Understand user intent  

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Microphone for voice input (optional)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/attitudebmw007-lab/jarvis.git
cd jarvis
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your API keys
```

5. Run JARVIS:
```bash
python main.py
```

## Usage

### Voice Mode
```bash
python main.py --voice
```
Speak your commands naturally. JARVIS will listen, process, and respond.

### Chat Mode
```bash
python main.py --chat
```
Type your questions and commands. Press Enter to submit.

### Combined Mode (Default)
```bash
python main.py
```
Use both voice and text interface together.

## Project Structure

```
jarvis/
├── main.py                 # Main entry point
├── requirements.txt        # Project dependencies
├── .env.example           # Environment variables template
├── config.py              # Configuration settings
├── README.md              # This file
│
├── core/
│   ├── __init__.py
│   ├── jarvis.py          # Main JARVIS class
│   ├── voice.py           # Voice recognition module
│   └── nlp.py             # Natural language processing
│
├── modules/
│   ├── __init__.py
│   ├── ai_response.py     # AI response generation
│   ├── automation.py      # Task automation
│   ├── chat.py            # Chat interface
│   └── commands.py        # Command handling
│
├── utils/
│   ├── __init__.py
│   ├── logger.py          # Logging utility
│   └── helpers.py         # Helper functions
│
└── data/
    ├── commands.json      # Predefined commands
    └── responses.json     # Response templates
```

## API Keys Required

- **OpenAI API Key** - For AI responses (ChatGPT)
  - Sign up at https://platform.openai.com
  - Get your API key from settings

- **Google Cloud Speech-to-Text** (Optional) - For advanced voice recognition
  - Set up at https://cloud.google.com

## Commands

Example commands JARVIS understands:

```
"What's the weather?"
"Set a reminder for 3 PM"
"Open Notepad"
"Tell me a joke"
"What's 5 plus 3?"
"Play music"
"Take a screenshot"
"System status"
```

## Configuration

Edit `config.py` to customize:
- Voice recognition language
- AI response style
- Automation tasks
- Response speed
- Wake word detection

## Troubleshooting

### Microphone not detected
- Check system audio settings
- Run: `python -m pip install --upgrade pyaudio`
- On Mac: `brew install portaudio && pip install pyaudio`

### API Key errors
- Verify your API keys in `.env`
- Check API usage limits
- Ensure keys have proper permissions

### Voice recognition issues
- Speak clearly and at normal pace
- Reduce background noise
- Check microphone permissions

## Development

Contribute to JARVIS:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Submit a Pull Request

## Future Enhancements

- [ ] Home automation integration (IoT devices)
- [ ] Machine learning for personalization
- [ ] Multi-language support
- [ ] Desktop GUI interface
- [ ] Web dashboard
- [ ] Mobile app integration
- [ ] Advanced emotion detection
- [ ] Real-time translation

## License

MIT License - See LICENSE file for details

## Author

Created by Ajay

## Support

For issues and questions, please create an issue on GitHub or contact support.

---

**Note**: This is an educational project inspired by JARVIS from Iron Man. It's a fun way to learn AI, voice recognition, and automation!
