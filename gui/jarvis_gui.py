"""GUI Interface for JARVIS using Tkinter."""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
from datetime import datetime
from core.jarvis import JARVIS
from utils.logger import setup_logger
import config

logger = setup_logger(__name__)

class JARVISGui:
    """GUI Interface for JARVIS AI Assistant."""
    
    def __init__(self, root):
        """Initialize GUI.
        
        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title("JARVIS - AI Assistant")
        self.root.geometry("900x700")
        self.root.configure(bg="#1a1a1a")
        
        # Initialize JARVIS
        self.jarvis = None
        self.response_style = tk.StringVar(value='casual')
        
        self.setup_ui()
        self.start_jarvis()
    
    def setup_ui(self):
        """Setup the user interface."""
        # Header
        header = tk.Frame(self.root, bg="#2d2d2d")
        header.pack(fill=tk.X, padx=10, pady=10)
        
        title = tk.Label(
            header,
            text="🤖 JARVIS - AI Assistant",
            font=("Arial", 24, "bold"),
            bg="#2d2d2d",
            fg="#00ff00"
        )
        title.pack()
        
        # Control Panel
        control_frame = tk.Frame(self.root, bg="#1a1a1a")
        control_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Response Style
        style_label = tk.Label(
            control_frame,
            text="Response Style:",
            bg="#1a1a1a",
            fg="#ffffff"
        )
        style_label.pack(side=tk.LEFT, padx=5)
        
        styles = ['casual', 'formal', 'technical', 'humorous']
        style_dropdown = ttk.Combobox(
            control_frame,
            textvariable=self.response_style,
            values=styles,
            state='readonly',
            width=12
        )
        style_dropdown.pack(side=tk.LEFT, padx=5)
        
        # Status
        self.status_label = tk.Label(
            control_frame,
            text="● Online",
            bg="#1a1a1a",
            fg="#00ff00",
            font=("Arial", 10, "bold")
        )
        self.status_label.pack(side=tk.RIGHT, padx=10)
        
        # Chat Display
        chat_label = tk.Label(
            self.root,
            text="Conversation",
            bg="#1a1a1a",
            fg="#00ff00",
            font=("Arial", 12, "bold")
        )
        chat_label.pack(anchor=tk.W, padx=10, pady=(10, 0))
        
        self.chat_display = scrolledtext.ScrolledText(
            self.root,
            height=15,
            width=100,
            bg="#2d2d2d",
            fg="#00ff00",
            insertbackground="#00ff00",
            font=("Courier", 10),
            wrap=tk.WORD
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.chat_display.config(state=tk.DISABLED)
        
        # Input Frame
        input_frame = tk.Frame(self.root, bg="#1a1a1a")
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        input_label = tk.Label(
            input_frame,
            text="You:",
            bg="#1a1a1a",
            fg="#ffffff"
        )
        input_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.user_input = tk.Entry(
            input_frame,
            bg="#2d2d2d",
            fg="#ffffff",
            insertbackground="#ffffff",
            font=("Arial", 11),
            width=100
        )
        self.user_input.pack(fill=tk.X, pady=5)
        self.user_input.bind('<Return>', self.send_message)
        
        # Button Frame
        button_frame = tk.Frame(input_frame, bg="#1a1a1a")
        button_frame.pack(fill=tk.X, pady=5)
        
        send_btn = tk.Button(
            button_frame,
            text="📤 Send",
            bg="#00ff00",
            fg="#000000",
            font=("Arial", 10, "bold"),
            command=self.send_message,
            width=15
        )
        send_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(
            button_frame,
            text="🗑️  Clear",
            bg="#ff6666",
            fg="#ffffff",
            font=("Arial", 10, "bold"),
            command=self.clear_chat,
            width=15
        )
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        exit_btn = tk.Button(
            button_frame,
            text="❌ Exit",
            bg="#666666",
            fg="#ffffff",
            font=("Arial", 10, "bold"),
            command=self.root.quit,
            width=15
        )
        exit_btn.pack(side=tk.LEFT, padx=5)
        
        # Add welcome message
        self.add_message("JARVIS", "Hello! I'm JARVIS, your AI assistant. How can I help you today?")
    
    def start_jarvis(self):
        """Start JARVIS in background thread."""
        try:
            self.jarvis = JARVIS(response_style=self.response_style.get())
            logger.info("JARVIS GUI initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing JARVIS: {str(e)}")
            messagebox.showerror("Error", f"Failed to initialize JARVIS: {str(e)}")
    
    def add_message(self, sender, message):
        """Add message to chat display.
        
        Args:
            sender: Message sender (You or JARVIS)
            message: Message text
        """
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        self.chat_display.config(state=tk.NORMAL)
        
        if sender == "You":
            self.chat_display.insert(tk.END, f"\n[{timestamp}] ", "time")
            self.chat_display.insert(tk.END, f"{sender}: ", "user")
        else:
            self.chat_display.insert(tk.END, f"\n[{timestamp}] ", "time")
            self.chat_display.insert(tk.END, f"🤖 {sender}: ", "assistant")
        
        self.chat_display.insert(tk.END, f"{message}\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
        
        # Configure tags
        self.chat_display.tag_config("time", foreground="#888888")
        self.chat_display.tag_config("user", foreground="#00ff00", font=("Courier", 10, "bold"))
        self.chat_display.tag_config("assistant", foreground="#ffff00", font=("Courier", 10, "bold"))
    
    def send_message(self, event=None):
        """Send user message to JARVIS.
        
        Args:
            event: Tkinter event (from Enter key)
        """
        user_message = self.user_input.get().strip()
        
        if not user_message:
            return
        
        # Display user message
        self.add_message("You", user_message)
        self.user_input.delete(0, tk.END)
        
        # Process in background thread
        thread = threading.Thread(
            target=self.process_message,
            args=(user_message,),
            daemon=True
        )
        thread.start()
    
    def process_message(self, user_input):
        """Process message and get JARVIS response.
        
        Args:
            user_input: User's input message
        """
        try:
            response = self.jarvis.process_input(user_input)
            self.add_message("JARVIS", response)
        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")
            self.add_message("JARVIS", f"I encountered an error: {str(e)}")
    
    def clear_chat(self):
        """Clear chat history."""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state=tk.DISABLED)
        self.add_message("JARVIS", "Chat cleared. How can I help you?")

def launch_gui():
    """Launch JARVIS GUI."""
    root = tk.Tk()
    app = JARVISGui(root)
    root.mainloop()

if __name__ == '__main__':
    launch_gui()
