

# WhatsApp Intent Classifier

This project automatically finds the user's intent in WhatsApp-like chat conversations using a pre-trained AI model. It classifies each conversation into one of these five types:
- Book Appointment
- Product Inquiry
- Pricing Negotiation
- Support Request
- Follow-Up

## How to Use

1. Install requirements:
    ```
    pip install -r requirements.txt
    ```
2. Run the main script:
    ```
    python main.py
    ```
3. Check the results:
    - JSON file: `data/output/predictions.json`
    - CSV file: `data/output/predictions.csv`

## Project Files

- `preprocessor.py` — cleans and prepares chat messages
- `classifier.py` — predicts intent
- `predictor.py` — handles one or many conversations
- `main.py` — runs the complete process
- `requirements.txt` — list of required python packages

## Sample Output

You will get files showing the predicted intent for each chat conversation.

![Sample Output](images/sample_output.png)


## Limitations

- The model may not always be accurate.
- It works best on simple English text.
- Only five types of intent are supported.
- It does not work with images, videos, or non-English text.

## Edge Cases

- Very short conversations may not be classified well.
- If the conversation mixes topics, results might be wrong.
- Too much slang, spelling errors, or very informal language may confuse the model.

---

**This project is for learning and demo purposes only.**

