# Simplified preprocessor.py
import re
import string

class MessagePreprocessor:
    def __init__(self):
        # Simplified emoji pattern
        self.emoji_pattern = re.compile(
            r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]+',
            flags=re.UNICODE
        )
    
    def clean_text(self, text):
        """Clean individual message text"""
        # Convert to lowercase
        text = text.lower()
        
        # Remove emojis
        text = self.emoji_pattern.sub(r'', text)
        
        # Remove URLs
        text = re.sub(r'http\S+|www.\S+', '', text)
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        return text.strip()
    
    def extract_conversation_context(self, messages, last_n=5):
        """Extract and combine recent messages for context"""
        # Take last N messages
        recent_messages = messages[-last_n:] if len(messages) > last_n else messages
        
        # Separate user and agent messages
        user_messages = []
        agent_messages = []
        
        for msg in recent_messages:
            cleaned_text = self.clean_text(msg['text'])
            if msg['sender'] == 'user':
                user_messages.append(cleaned_text)
            else:
                agent_messages.append(cleaned_text)
        
        # Combine with context markers
        context = "User messages: " + " | ".join(user_messages)
        context += " Agent messages: " + " | ".join(agent_messages)
        
        return context, user_messages, agent_messages