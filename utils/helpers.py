"""Helper utility functions."""

from textwrap import wrap
from datetime import datetime

def format_response(text, max_width=80):
    """Format response text for display.
    
    Args:
        text: Text to format
        max_width: Maximum line width
        
    Returns:
        Formatted text
    """
    return '\n'.join(wrap(text, max_width))

def get_greeting():
    """Get time-appropriate greeting.
    
    Returns:
        Greeting string
    """
    hour = datetime.now().hour
    
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

def is_question(text):
    """Check if text is a question.
    
    Args:
        text: Text to check
        
    Returns:
        Boolean
    """
    return text.strip().endswith('?')

def sanitize_input(text):
    """Sanitize user input.
    
    Args:
        text: Input text
        
    Returns:
        Sanitized text
    """
    return text.strip().lower()
