"""AI response generation module using OpenAI."""

import openai
from utils.logger import setup_logger
import config

logger = setup_logger(__name__)

class AIResponseGenerator:
    """Generate AI responses using OpenAI API."""
    
    def __init__(self, response_style='casual'):
        """Initialize AI response generator.
        
        Args:
            response_style: Style of responses
        """
        openai.api_key = config.OPENAI_API_KEY
        self.response_style = response_style
        self.model = config.AI_MODEL
        self.temperature = config.RESPONSE_TEMPERATURE
        self.max_tokens = config.MAX_TOKENS
        
        if not config.OPENAI_API_KEY:
            logger.warning("OpenAI API key not configured")
    
    def generate_response(self, user_input: str) -> str:
        """Generate AI response to user input.
        
        Args:
            user_input: User's input text
            
        Returns:
            AI-generated response
        """
        try:
            # Create system prompt with style guidance
            style_instruction = config.RESPONSE_STYLES.get(
                self.response_style,
                config.RESPONSE_STYLES['casual']
            )
            
            system_prompt = f"{config.JARVIS_SYSTEM_PROMPT}\n{style_instruction}"
            
            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            
            # Extract response text
            ai_response = response.choices[0].message.content.strip()
            logger.debug(f"AI response generated: {ai_response[:50]}...")
            
            return ai_response
            
        except openai.error.AuthenticationError:
            logger.error("Invalid OpenAI API key")
            return "I'm having trouble connecting to the AI service. Please check your API key."
        except openai.error.RateLimitError:
            logger.error("OpenAI rate limit exceeded")
            return "I'm being used too much right now. Please try again in a moment."
        except Exception as e:
            logger.error(f"AI response generation error: {str(e)}")
            return f"I encountered an error: {str(e)}"
