"""Natural Language Processing module."""

import re
from typing import Dict, List, Tuple
from utils.logger import setup_logger

logger = setup_logger(__name__)

class NLPProcessor:
    """Process and analyze natural language."""
    
    def __init__(self):
        """Initialize NLP processor."""
        self.intents = {
            'greeting': ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon'],
            'question': ['what', 'how', 'why', 'when', 'where', 'who', 'which'],
            'command': ['do', 'set', 'open', 'play', 'create', 'show', 'tell'],
            'farewell': ['bye', 'goodbye', 'exit', 'quit', 'see you', 'farewell']
        }
    
    def detect_intent(self, text: str) -> str:
        """Detect user intent from text.
        
        Args:
            text: Input text
            
        Returns:
            Detected intent
        """
        text_lower = text.lower()
        
        for intent, keywords in self.intents.items():
            for keyword in keywords:
                if keyword in text_lower:
                    logger.debug(f"Detected intent: {intent}")
                    return intent
        
        return 'general'
    
    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """Extract entities from text.
        
        Args:
            text: Input text
            
        Returns:
            Dictionary of extracted entities
        """
        entities = {
            'numbers': re.findall(r'\b\d+\b', text),
            'times': re.findall(r'\d{1,2}:\d{2}', text),
            'emails': re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text),
            'urls': re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        }
        
        return entities
    
    def tokenize(self, text: str) -> List[str]:
        """Tokenize text into words.
        
        Args:
            text: Input text
            
        Returns:
            List of tokens
        """
        return text.lower().split()
    
    def similarity(self, text1: str, text2: str) -> float:
        """Calculate text similarity.
        
        Args:
            text1: First text
            text2: Second text
            
        Returns:
            Similarity score (0-1)
        """
        words1 = set(self.tokenize(text1))
        words2 = set(self.tokenize(text2))
        
        if not words1 or not words2:
            return 0.0
        
        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))
        
        return intersection / union if union > 0 else 0.0
