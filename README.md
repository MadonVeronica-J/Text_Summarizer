# Text Summarizer

A web-based application that intelligently shortens long pieces of text into concise summaries — using both **Extractive** and **Abstractive** techniques.  
Built with **Python** and **Django**, this tool helps users quickly grasp key insights from lengthy content.

---

## Features
- **Extractive Summarization** — Select key sentences directly from the input text.  
- **Abstractive Summarization** — Generates summaries in natural, rephrased language.  
- **Interactive Dashboard** — Simple UI for text input and output.  
- **Customizable** — Set number of sentences (Extractive) or word limit (Abstractive).  
- **Clean Summary Output** — Ready for copying, saving, or further processing.
- **Downloadable Summary** — Generated summary can be downloaded as PDF or Word Document. 
- **History** — Stores every summary generated and can be viewed when needed.

---

## 🛠️ Technologies Used
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python (Django Framework)  
- **Libraries:**  
  - NLTK / SpaCy (for Extractive Summarization)  
  - Transformers (for Abstractive Summarization)  
- **Database:** SQLite  
- **Version Control:** Git & GitHub

---

## Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/text-summarizer.git
cd text-summarizer
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Server
```bash
python manage.py runserver
```

Then open http://127.0.0.1:8000/in your browser.

## How It Works

1. The user enters text in the dashboard.
2. Chooses either:
   - Extract to Summary → enter number of sentences
   - Abstract to Summary → enter max word count
3. Clicks Summarize → The system generates and displays the result.

## Screenshots
Abractive Summary (maximum 100 words):
<img width="918" height="754" alt="Abstractive output" src="https://github.com/user-attachments/assets/1f6a82e3-b8b1-4bec-93ed-c23aed61b5fd" />

Extractive Summary (5 sentences):
<img width="858" height="846" alt="Extractive output" src="https://github.com/user-attachments/assets/d9751752-c9fc-4cde-94c5-bf8d77ea4c3b" />


