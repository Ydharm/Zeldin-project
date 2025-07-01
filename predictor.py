import json
import pandas as pd

class ConversationPredictor:
    def __init__(self, preprocessor, classifier):
        self.preprocessor = preprocessor
        self.classifier = classifier
    
    def predict_single(self, conversation):
        """Predict intent for one conversation"""
        conv_id = conversation['conversation_id']
        messages = conversation['messages']
        
        # Preprocess
        context, user_msgs, _ = self.preprocessor.extract_conversation_context(messages)
        
        # Classify
        intent, confidence, rationale = self.classifier.classify(context, user_msgs)
        
        return {
            "conversation_id": conv_id,
            "predicted_intent": intent,
            "confidence": round(confidence, 3),
            "rationale": rationale
        }
    
    def predict_batch(self, input_file, output_json_file, output_csv_file):
        """Process multiple conversations"""
        # Read input
        print(f"Reading {input_file}...")
        with open(input_file, 'r') as f:
            data = json.load(f)
        
        # Make sure it's a list
        if not isinstance(data, list):
            data = [data]
        
        results = []
        
        # Process each conversation
        print(f"Processing {len(data)} conversations...")
        for i, conv in enumerate(data):
            print(f"  Processing conversation {i+1}/{len(data)}...")
            result = self.predict_single(conv)
            results.append(result)
            print(f"    Intent: {result['predicted_intent']} (confidence: {result['confidence']})")
        
        # Save as JSON
        with open(output_json_file, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Saved JSON results to {output_json_file}")
        
        # Save as CSV
        df = pd.DataFrame(results)
        df.to_csv(output_csv_file, index=False)
        print(f"Saved CSV results to {output_csv_file}")
        
        return results