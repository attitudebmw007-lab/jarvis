"""Voice recognition and text-to-speech module."""

import speech_recognition as sr
import pyttsx3
from utils.logger import setup_logger
import config

logger = setup_logger(__name__)

class VoiceRecognition:
    """Handle voice recognition and text-to-speech."""
    
    def __init__(self):
        """Initialize voice recognition and TTS."""
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone(device_index=config.MICROPHONE_INDEX)
        
        # Initialize TTS engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', config.VOICE_RATE)
        self.engine.setProperty('volume', config.VOICE_VOLUME)
        
        logger.info("Voice recognition initialized")
    
    def listen(self, timeout=10):
        """Listen for audio input and convert to text.
        
        Args:
            timeout: Listening timeout in seconds
            
        Returns:
            Recognized text or None
        """
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=timeout)
            
            # Recognize speech using Google Speech Recognition
            text = self.recognizer.recognize_google(
                audio,
                language=config.VOICE_LANGUAGE
            )
            logger.debug(f"Recognized: {text}")
            return text
            
        except sr.UnknownValueError:
            logger.warning("Could not understand audio")
            return None
        except sr.RequestError as e:
            logger.error(f"Speech recognition error: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Voice recognition error: {str(e)}")
            return None
    
    def speak(self, text):
        """Convert text to speech.
        
        Args:
            text: Text to speak
        """
        try:
            logger.debug(f"Speaking: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            logger.error(f"Text-to-speech error: {str(e)}")
