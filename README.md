# 📚 Vocabulary Trainer

A Python-based command-line app for learning English–Hebrew vocabulary.
Practice, test, and track your progress with themed vocabulary units like Fruits, School, and Nature.

---

## 🚀 Features

### 🧩 Editing Mode

* Add, update, or delete vocabulary words
* Organize words into units (e.g., Unit 1 = Fruits & Vegetables)

### 📖 Training Mode

* See an English word, then press Enter to reveal its Hebrew meaning
* Each practiced word is logged in `repeat_log.json`

### 🧪 Testing Mode

* Take a quiz: type the Hebrew meaning of each English word
* Get immediate feedback and a final score

### ☁️ S3 Integration (Boto3)

* Your `repeat_log.json` file is automatically uploaded to an AWS S3 bucket after each training session

---

## 🧠 Project Structure

```
📦 vocabulary_trainer
├── main.py                # Main menu interface
├── vocab_utils.py         # Shared utility functions
├── editing.py             # Word editing mode
├── training.py            # Word training mode
├── testing.py             # Quiz/testing mode
├── vocab_hebrew.json      # Vocabulary database
├── repeat_log.json        # Practice tracking file
```

---

## 🌍 Hebrew Explanation (הסבר בעברית)

**Vocabulary Trainer** הוא כלי תרגול לאוצר מילים באנגלית-עברית.

* 🧩 מצב עריכה: ניתן להוסיף ולעדכן מילים
* 📖 מצב תרגול: רואים מילה באנגלית ולוחצים Enter כדי לגלות את התרגום
* 🧪 מצב מבחן: מקלידים את התרגום לעברית ומקבלים ציון
* ☁️ כל תרגול נרשם ומועלה ל-AWS S3

---

## ✅ Getting Started

1. Clone this repo:

```bash
git clone git@github.com:NadiaGerman/vocabulary_trainer.git
```

2. Run the app:

```bash
python3 main.py
```

---

## ✨ Credits

Developed by Nadia German ✨

This tool is part of a full-stack project for learning Hebrew vocabulary efficiently.

---

## 📬 Questions?

Reach out via [GitHub](https://github.com/NadiaGerman) or open an issue.
