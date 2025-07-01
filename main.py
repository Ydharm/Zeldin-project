from preprocessor import MessagePreprocessor
from classifier import IntentClassifier
from predictor import ConversationPredictor
import json
import os

def create_sample_data():
    """Create test data"""
    print("Creating sample data...")
    
    sample_data = [
    {
        "conversation_id": "conv_001",
        "messages": [
            {"sender": "user", "text": "Hi, I'm looking for a 2BHK apartment in Dubai Marina"},
            {"sender": "agent", "text": "Great! We have several options available. What's your budget range?"},
            {"sender": "user", "text": "Around 100-120k per year"},
            {"sender": "agent", "text": "Perfect! I have 3 properties that match your criteria"},
            {"sender": "user", "text": "Can we schedule a site visit this weekend? Saturday morning would be ideal"}
        ]
    },
    {
        "conversation_id": "conv_002",
        "messages": [
            {"sender": "user", "text": "What kind of laptops do you have available?"},
            {"sender": "agent", "text": "We have Dell, HP, Lenovo, and Apple laptops"},
            {"sender": "user", "text": "I need something for gaming. What do you recommend?"},
            {"sender": "agent", "text": "For gaming, I'd suggest our ASUS ROG or MSI Gaming series"},
            {"sender": "user", "text": "What are the specs of the ASUS ROG?"}
        ]
    },
    {
        "conversation_id": "conv_003",
        "messages": [
            {"sender": "user", "text": "I saw your premium package is $199. That's quite expensive"},
            {"sender": "agent", "text": "I understand your concern. This package includes many premium features"},
            {"sender": "user", "text": "Can you offer any discount? Maybe 20% off?"},
            {"sender": "agent", "text": "Let me check what I can do for you"},
            {"sender": "user", "text": "If you can do $150, I'll sign up today"}
        ]
    },
    {
        "conversation_id": "conv_004",
        "messages": [
            {"sender": "user", "text": "My internet connection keeps dropping every few minutes"},
            {"sender": "agent", "text": "I'm sorry to hear that. When did this issue start?"},
            {"sender": "user", "text": "Started yesterday evening. I've already restarted the router"},
            {"sender": "agent", "text": "I see. Let me run a diagnostic on your connection"},
            {"sender": "user", "text": "Please fix this urgently. I have important meetings today"}
        ]
    },
    {
        "conversation_id": "conv_005",
        "messages": [
            {"sender": "user", "text": "Hi, I submitted a loan application last Monday"},
            {"sender": "agent", "text": "Hello! Let me check the status for you"},
            {"sender": "user", "text": "It's been a week now. Any updates?"},
            {"sender": "agent", "text": "I can see your application is under review"},
            {"sender": "user", "text": "When can I expect a decision? I'm following up as you asked me to"}
        ]
    },
    {
        "conversation_id": "conv_006",
        "messages": [
            {"sender": "user", "text": "Do you have the iPhone 15 Pro in stock?"},
            {"sender": "agent", "text": "Yes, we have it in all colors except blue"},
            {"sender": "user", "text": "Great! What's the price for the 256GB version?"},
            {"sender": "agent", "text": "The 256GB is $1099"},
            {"sender": "user", "text": "Can I come to your store today to see it?"}
        ]
    }
]
    
    # Create directories
    os.makedirs('data', exist_ok=True)
    os.makedirs('data/output', exist_ok=True)
    
    # Save sample data
    with open('data/input_conversations.json', 'w') as f:
        json.dump(sample_data, f, indent=2)
    
    print("Sample data created in data/input_conversations.json")
    return True

def main():
    print("=== WhatsApp Intent Classifier ===\n")
    
    # Always create sample data first
    create_sample_data()
    
    # Verify file exists
    if not os.path.exists('data/input_conversations.json'):
        print("Error: Could not create sample data file!")
        return
    
    # Check if file is not empty
    if os.path.getsize('data/input_conversations.json') == 0:
        print("Error: Sample data file is empty!")
        create_sample_data()  # Try again
    
    # Initialize components
    print("\nSetting up components...")
    preprocessor = MessagePreprocessor()
    print("✓ Preprocessor ready")
    
    classifier = IntentClassifier()
    print("✓ Classifier ready")
    
    predictor = ConversationPredictor(preprocessor, classifier)
    print("✓ Predictor ready\n")
    
    # Process conversations
    try:
        predictor.predict_batch(
            'data/input_conversations.json',
            'data/output/predictions.json',
            'data/output/predictions.csv'
        )
    except Exception as e:
        print(f"Error during prediction: {e}")
        print("\nTrying to create fresh sample data...")
        create_sample_data()
        print("Please run the program again.")
    
    print("\n=== Done! ===")
    print("Check the results in:")
    print("  - data/output/predictions.json")
    print("  - data/output/predictions.csv")

if __name__ == "__main__":
    main()