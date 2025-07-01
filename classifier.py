from transformers import pipeline

class IntentClassifier:
    def __init__(self):
        print("Loading model... This may take a minute...")
        # Use simple zero-shot classification
        self.classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli"
        )
        
        # Define intent labels
        self.intent_labels = [
            "Book Appointment",
            "Product Inquiry", 
            "Pricing Negotiation",
            "Support Request",
            "Follow-Up"
        ]
    
    def classify(self, conversation_text, user_messages):
        """Classify the intent"""
        # Run classification
        result = self.classifier(
            conversation_text,
            candidate_labels=self.intent_labels
        )
        
        # Get results
        predicted_intent = result['labels'][0]
        confidence = result['scores'][0]
        
        # Simple rationale
        rationale = f"Based on the conversation, this seems to be about {predicted_intent.lower()}"
        
        return predicted_intent, confidence, rationale