

# 🧠 AI Wiki Quiz Generator

An end-to-end **AI-powered quiz generation system** that takes a **Wikipedia article URL**, scrapes the content, and automatically generates a **multiple-choice quiz** using an LLM.
Built as part of a technical assignment for **DeepKlarity Technologies**.

---

## 🚀 Features

### ✅ Tab 1 – Generate Quiz

* Accepts a Wikipedia article URL
* Scrapes article content using **BeautifulSoup**
* Generates quiz questions using **LLM logic (Gemini-compatible)**
* Each quiz includes:

  * Question
  * 4 Options
  * Correct Answer
  * Explanation
  * Difficulty level
* Stores generated quizzes in **MySQL database**
* Returns structured **JSON API response**

### ✅ Tab 2 – Past Quizzes

* Fetches previously generated quizzes from database
* Displays quiz history
* Enables reusability of past quiz data

---

## 🛠 Tech Stack

### Backend

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **MySQL**
* **BeautifulSoup**
* **Uvicorn**

### Frontend

* **HTML**
* **CSS**
* **JavaScript (Fetch API)**

---

## 📂 Project Structure

```
ai-wiki-quiz/
│
├── main.py                 # FastAPI app
├── requirements.txt
├── .env.example
│
├── db/
│   ├── database.py
│   ├── models.py
│   ├── session.py
│   └── create_tables.py
│
├── utils/
│   ├── wiki_scraper.py
│   ├── wiki_validator.py
│   └── quiz_generator.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/kushwanthkumar73/ai-wiki-quiz
cd ai-wiki-quiz
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create `.env` file:

```
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/ai_wiki_quiz
```

### 5️⃣ Create Database Tables

```bash
python -m db.create_tables
```

### 6️⃣ Run Backend Server

```bash
uvicorn main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

---

## 🔌 API Endpoints

| Method | Endpoint          | Description                 |
| ------ | ----------------- | --------------------------- |
| GET    | `/health`         | Health check                |
| POST   | `/validate-url`   | Validate Wikipedia URL      |
| POST   | `/scrape-article` | Scrape article content      |
| POST   | `/generate-quiz`  | Generate quiz & store in DB |
| GET    | `/quizzes`        | Fetch past quizzes          |

---

## 🧪 Sample Request

```json
POST /generate-quiz
{
  "url": "https://en.wikipedia.org/wiki/Alan_Turing"
}
```

---

## 📸 Screenshots & Testing

* Quiz generation tested with multiple Wikipedia URLs
* Backend returns valid JSON responses
* Database persistence verified using MySQL

---

## 🎯 Assignment Compliance

✔ Python backend (FastAPI)
✔ Wikipedia scraping (HTML only)
✔ Quiz generation with explanations & difficulty
✔ MySQL database storage
✔ Frontend UI with two tabs
✔ Modular, readable code
✔ Error handling implemented

---

