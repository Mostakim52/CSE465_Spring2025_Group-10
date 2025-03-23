# RNN Text Classification

## 📌 Team Contribution Table

| Team Member | Contribution |
|-------------|-------------|
| Member 1    | Data Preprocessing |
| Member 2    | Augmentation, Model Development & Training |
| Member 3    | Evaluation |

---

## 📝 Data Augmentation Methods
For improving the dataset, the following augmentation techniques were applied:
- **Synonym Replacement**: Replacing words with their synonyms.
- **Back Translation**: Translating text to another language and back.
- **Random Insertion & Deletion**: Inserting and deleting random words.
- **Text Paraphrasing**: Using NLP models to rephrase claims.

The augmented dataset is stored inside the `Augmented Data` folder, along with labels.

---

## 📊 Final Results (5-Fold Cross-Validation)

| Fold | Accuracy | Precision | Recall | F1 Score |
|------|----------|------------|--------|----------|
| 1    | 0.8280   | 0.8267     | 0.8280 | 0.8259   |
| 2    | 0.9345   | 0.9382     | 0.9345 | 0.9332   |
| 3    | 0.9232   | 0.9269     | 0.9232 | 0.9239   |
| 4    | 0.8390   | 0.8455     | 0.8390 | 0.8408   |
| 5    | 0.9569   | 0.9574     | 0.9569 | 0.9567   |
| **Average** | **0.8963** | **0.8989** | **0.8963** | **0.8961** |

---

## 📊 Confusion Matrix
```
![image](https://github.com/user-attachments/assets/069e503f-0306-4e1b-b019-17d08e30cc89)
![image](https://github.com/user-attachments/assets/8c2ce2e0-edc4-4244-a701-98c21d175fba)


```

## 📂 Repository Structure
```
📦 Project Repository
├── 📁 Augmented Data   # Augmented dataset & labels
├── 📄 train.ipynb      # Training notebook
├── 📄 model.h5         # Saved trained model
├── 📄 test_script.py   # Prediction script using the trained model
├── 📄 Network.jpg      # Block diagram of the neural network
├── 📄 README.md        # Project documentation
```

---

3️⃣ **Modify `test_script.py` to input new text samples.**

---

### 🎯 Conclusion
The RNN model achieved an **average accuracy of 95.79%** using 5-fold cross-validation, demonstrating strong performance in text classification.

