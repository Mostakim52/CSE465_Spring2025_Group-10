# -*- coding: utf-8 -*-
"""Project assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hG6Sr4lkvVeDzORTJtM5ldSKTqQ48CS7

#Data augmentation
"""

# Required imports
import pandas as pd
import random


# Load dataset (Update path if loading from Drive)
df = pd.read_csv("full_df.csv")  # Or replace with the correct path

# Drop unnecessary/empty columns if needed
if 'Statement' in df.columns:
    df = df.drop(columns=['Statement'])

# Extract values
claims = df['Claim'].tolist()
labels = df['Label'].tolist()
domains = df['Domain'].tolist()

# Define simple word shuffling function
def basic_augment(sentence):
    words = sentence.split()
    if len(words) <= 3:
        return sentence
    middle = words[1:-1]
    random.shuffle(middle)
    return ' '.join([words[0]] + middle + [words[-1]])

# Set seed for reproducibility
random.seed(42)

# How many samples to augment? (30%)
num_to_augment = int(len(claims) * 0.30)

# Sample random indices
sample_indices = random.sample(range(len(claims)), num_to_augment)

# Create augmented data
augmented_claims = [basic_augment(claims[i]) for i in sample_indices]
augmented_labels = [labels[i] for i in sample_indices]
augmented_domains = [domains[i] for i in sample_indices]

# Create DataFrame for augmented data
aug_df = pd.DataFrame({
    'Claim': augmented_claims,
    'Label': augmented_labels,
    'Domain': augmented_domains
})

# Combine original and augmented datasets
augmented_full_df = pd.concat([df, aug_df], ignore_index=True)

# Shuffle the final dataset (optional but recommended)
augmented_full_df = augmented_full_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save to new CSV
augmented_full_df.to_csv("augmented_full_df.csv", index=False)

# Preview
print("Original dataset size:", len(df))
print("Augmented dataset size:", len(aug_df))
print("Total size after augmentation:", len(augmented_full_df))
augmented_full_df.head()



"""#RNN + 5-Fold CV"""

!pip install tensorflow


import numpy as np
from sklearn.model_selection import KFold
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from tensorflow.keras.utils import to_categorical

# Load your dataset
df = pd.read_csv("augmented_full_df.csv")  # Update with your file path
texts = df['Claim'].astype(str).tolist()
labels = df['Label'].tolist()

# One-hot encode labels
num_classes = len(set(labels))
y = to_categorical(labels, num_classes=num_classes)

# Tokenize text
tokenizer = Tokenizer(num_words=10000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

# Pad sequences
max_length = max(len(seq) for seq in sequences)
X = pad_sequences(sequences, maxlen=max_length, padding='post')

# 5-Fold Cross-Validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)
fold = 1
accuracy_scores = []

for train_index, val_index in kf.split(X):
    X_train, X_val = X[train_index], X[val_index]
    y_train, y_val = y[train_index], y[val_index]

    #Vanilla RNN model
    model = Sequential([
        Embedding(input_dim=10000, output_dim=100, input_length=max_length),
        SimpleRNN(64, return_sequences=False),
        Dense(32, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    #Train
    print(f"Training Fold {fold}...")
    model.fit(X_train, y_train, epochs=5, batch_size=32, verbose=1)

    #Evaluate
    loss, acc = model.evaluate(X_val, y_val, verbose=1)
    accuracy_scores.append(acc)
    print(f"Fold {fold} Accuracy: {acc:.4f}\n")
    fold += 1

# Final result
print("Average 5-Fold Accuracy:", np.mean(accuracy_scores))

# Save the trained model (after last fold)
model.save("rnn_text_classification_model.h5")  # Saves in .h5 format

# Save the tokenizer for inference
import pickle
with open("tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

print("Model and tokenizer saved successfully!")

import pandas as pd

# Assuming df contains your augmented dataset
# Replace 'Augmented_Text' and 'Label' with actual column names
df_augmented = pd.DataFrame({
    "Sample": df["Claim"],  # Text or filename
    "Label": df["Label"]    # Corresponding labels
})

# Save as CSV
df_augmented.to_csv("augmented_data_labels.csv", index=False)

print("CSV file saved successfully!")