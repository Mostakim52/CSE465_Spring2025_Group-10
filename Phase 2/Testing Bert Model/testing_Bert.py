from transformers import TFAutoModelForSequenceClassification, AutoTokenizer
import tensorflow as tf

# Path to your exported model folder
model_path = "../Bert Model Files/"

# Load the model and tokenizer
model = TFAutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Sample input - can put any statement inputs here false or true
claims = [
    "The Prime Minister of the UK is elected directly by the public.",
    "The Constitution of the US has 27 amendments."
]

# Tokenize input
inputs = tokenizer(claims, padding=True, truncation=True, return_tensors="tf")

# Get predictions
outputs = model(inputs)
preds = tf.argmax(outputs.logits, axis=1).numpy()

# Display predictions
for claim, pred in zip(claims, preds):
    print(f"Claim: {claim}\nPrediction: {'True' if pred == 1 else 'False'}\n")
