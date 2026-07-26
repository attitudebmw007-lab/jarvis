"""Command handling module."""

import json
import os
from utils.logger import setup_logger

logger = setup_logger(__name__)

class CommandHandler:
    """Handle predefined commands."""
    
    def __init__(self):
        """Initialize command handler."""
        self.commands = self._load_commands()
        logger.info(f"Loaded {len(self.commands)} commands")
    
    def _load_commands(self) -> dict:
        """Load commands from JSON file.
        
        Returns:
            Dictionary of commands
        """
        commands_file = 'data/commands.json'
        
        if os.path.exists(commands_file):
            try:
                with open(commands_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Error loading commands: {str(e)}")
        
        return self._get_default_commands()
    
    def _get_default_commands(self) -> dict:
        """Get default commands.
        
        Returns:
            Dictionary of default commands
        """
        return {
            'help': {
                'keywords': ['help', 'support', 'assist'],
                'response': 'I can help you with voice commands, chat, task automation, and answering questions. What would you like to do?'
            },
            'about': {
                'keywords': ['about', 'who are you', 'introduce'],
                'response': 'I am JARVIS, an AI assistant inspired by Iron Man\'s AI. I can help you with tasks, answer questions, and automate processes.'
            },
            'status': {
                'keywords': ['status', 'how are you'],
                'response': 'All systems operational. Ready to assist.'
            }
        }
    
    def handle(self, user_input: str) -> str:
        """Handle user command if it matches predefined commands.
        
        Args:
            user_input: User input
            
        Returns:
            Command response or None
        """
        input_lower = user_input.lower()
        
        for command_name, command_data in self.commands.items():
            keywords = command_data.get('keywords', [])
            for keyword in keywords:
                if keyword in input_lower:
                    logger.debug(f"Command executed: {command_name}")
                    return command_data.get('response', 'Command executed')
        
        return None
