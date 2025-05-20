
# 📘 Vocabulary Trainer – Function Cheat Sheet (English + Hebrew)

### `main()` – (main.py)  
**EN**: Displays the main menu and routes to editing, training, or testing.  
**HE**: מציג את התפריט הראשי ומפנה למצב עריכה, תרגול או מבחן.

---

### `editing_mode()` – (editing.py)  
**EN**: Shows editing menu: add, delete, update, list, or search words.  
**HE**: מציג תפריט לעריכת מילים: הוספה, מחיקה, עדכון, הצגה או חיפוש.

### `add_word()` – (editing.py)  
**EN**: Adds a new English-Hebrew word to a unit.  
**HE**: מוסיף זוג מילה-תרגום ליחידה.

### `delete_word()` – (editing.py)  
**EN**: Deletes a word from a selected unit.  
**HE**: מוחק מילה מהיחידה.

### `update_word()` – (editing.py)  
**EN**: Updates an existing word or its meaning.  
**HE**: מעדכן מילה קיימת או את התרגום.

### `list_words()` – (editing.py)  
**EN**: Lists all words in a selected unit.  
**HE**: מציג את כל המילים ביחידה.

### `search_word()` – (editing.py)  
**EN**: Searches all units for a word.  
**HE**: מחפש מילה בכל היחידות.

---

### `training_mode()` – (training.py)  
**EN**: Practice mode: show word, wait, then show meaning and log.  
**HE**: מצב תרגול: מציג מילה, ממתין ואז מציג תרגום ושומר ביומן.

---

### `testing_mode()` – (testing.py)  
**EN**: Quiz mode: enter Hebrew translation, get score.  
**HE**: מבחן: כותבים תרגום, מקבלים ציון.

---

### `load_vocab()` / `save_vocab()` – (vocab_utils.py)  
**EN**: Load or save vocabulary from/to JSON.  
**HE**: טוען או שומר את המילון מקובץ JSON.

### `load_repeat_log()` / `save_repeat_log()` – (vocab_utils.py)  
**EN**: Load or save the repetition log.  
**HE**: טוען או שומר את יומן התרגול.

### `log_word_repeat()` – (vocab_utils.py)  
**EN**: Logs repetition of a word each time it's practiced.  
**HE**: מתעד תרגול של מילה ביומן.

### `upload_log_to_s3()` – (vocab_utils.py)  
**EN**: Uploads the repeat log to your AWS S3 bucket.  
**HE**: מעלה את קובץ הלוג ל־S3 של AWS.

### `normalize_text()` – (vocab_utils.py)  
**EN**: Normalizes input for consistent matching.  
**HE**: מנרמל טקסט עברי/אנגלי כדי לאפשר השוואה תקינה.

### `get_unit_choice()` – (vocab_utils.py)  
**EN**: Shows unit menu and returns selected unit (1, 2, or 3).  
**HE**: מציג תפריט יחידות ומחזיר את היחידה שנבחרה.

### `find_word_index()` – (vocab_utils.py)  
**EN**: Finds the index of a word in a unit list or returns -1.  
**HE**: מחפש מילה ומחזיר את מיקומה או ‎-1‎ אם לא נמצאה.

### `ensure_unit_exists()` – (vocab_utils.py)  
**EN**: Ensures the unit exists in the vocabulary structure.  
**HE**: מוודא שהיחידה קיימת ואם לא – יוצר אותה.

### `search_word_global()` – (vocab_utils.py)  
**EN**: Searches for a word across all units.  
**HE**: מחפש מילה בכל היחידות הקיימות.
