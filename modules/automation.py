"""Task automation module."""

import subprocess
import os
from datetime import datetime
from utils.logger import setup_logger

logger = setup_logger(__name__)

class TaskAutomation:
    """Handle task automation."""
    
    def __init__(self):
        """Initialize task automation."""
        self.tasks = {
            'screenshot': self._take_screenshot,
            'open': self._open_application,
            'time': self._get_time,
            'date': self._get_date,
            'system': self._get_system_info
        }
        logger.info("Task automation initialized")
    
    def execute(self, user_input: str) -> str:
        """Execute automation task if applicable.
        
        Args:
            user_input: User input
            
        Returns:
            Task result or None
        """
        input_lower = user_input.lower()
        
        # Check for known tasks
        for task_name, task_func in self.tasks.items():
            if task_name in input_lower:
                logger.debug(f"Executing task: {task_name}")
                return task_func(user_input)
        
        return None
    
    def _take_screenshot(self, user_input: str) -> str:
        """Take a screenshot."""
        try:
            import pyautogui
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            pyautogui.screenshot(filename)
            logger.info(f"Screenshot saved: {filename}")
            return f"Screenshot saved as {filename}"
        except Exception as e:
            logger.error(f"Screenshot error: {str(e)}")
            return "I couldn't take a screenshot."
    
    def _open_application(self, user_input: str) -> str:
        """Open an application."""
        try:
            # Extract application name
            apps = {
                'notepad': 'notepad' if os.name == 'nt' else 'gedit',
                'calculator': 'calc' if os.name == 'nt' else 'gnome-calculator',
                'browser': 'start https://www.google.com' if os.name == 'nt' else 'open https://www.google.com'
            }
            
            for app_name, app_command in apps.items():
                if app_name in user_input.lower():
                    subprocess.Popen(app_command, shell=True)
                    logger.info(f"Opened: {app_name}")
                    return f"Opening {app_name}"
            
            return None
        except Exception as e:
            logger.error(f"Application open error: {str(e)}")
            return "I couldn't open that application."
    
    def _get_time(self, user_input: str) -> str:
        """Get current time."""
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}"
    
    def _get_date(self, user_input: str) -> str:
        """Get current date."""
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {current_date}"
    
    def _get_system_info(self, user_input: str) -> str:
        """Get system information."""
        try:
            import psutil
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            return f"CPU: {cpu_percent}% | Memory: {memory.percent}%"
        except Exception as e:
            logger.error(f"System info error: {str(e)}")
            return "I couldn't retrieve system information."
