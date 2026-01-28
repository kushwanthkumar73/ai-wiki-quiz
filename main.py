from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
import json

from utils.wiki_validator import validate_wikipedia_url
from utils.wiki_scraper import scrape_wikipedia_article
from utils.quiz_generator import generate_quiz

from db.session import get_db
from db.models import Article, Quiz   # ✅ IMPORT ARTICLE

app = FastAPI(title="DeepKlarity AI Wiki Quiz API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # frontend allow
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, OPTIONS
    allow_headers=["*"],
)

# -------------------------
# Health Check
# -------------------------
@app.get("/health")
def health_check():
    return {"status": "ok"}


# -------------------------
# Validate Wikipedia URL
# -------------------------
@app.post("/validate-url")
def validate_url(payload: dict):
    url = payload.get("url")

    if not url:
        raise HTTPException(status_code=400, detail="URL is required")

    is_valid, result = validate_wikipedia_url(url)

    if not is_valid:
        raise HTTPException(status_code=400, detail=result)

    return {"valid": True, "title": result}


# -------------------------
# Scrape Wikipedia Article
# -------------------------
@app.post("/scrape-article")
def scrape_article(payload: dict):
    url = payload.get("url")

    if not url:
        raise HTTPException(status_code=400, detail="URL is required")

    return scrape_wikipedia_article(url)


# -------------------------
# Generate Quiz + SAVE to DB 🔥
# -------------------------
@app.post("/generate-quiz")
def generate_quiz_api(payload: dict, db: Session = Depends(get_db)):
    url = payload.get("url")

    if not url:
        raise HTTPException(status_code=400, detail="URL is required")

    # 1️⃣ Scrape Wikipedia
    article_data = scrape_wikipedia_article(url)

    # 2️⃣ Check if article already exists
    article = db.query(Article).filter(Article.url == url).first()

    if not article:
        article = Article(
            url=url,
            title=article_data["title"],
            summary=article_data["summary"]
        )
        db.add(article)
        db.commit()
        db.refresh(article)

    # 3️⃣ Generate quiz using AI
    quiz_json = generate_quiz(article_data["full_text"])

    # 4️⃣ Save quiz
    quiz_record = Quiz(
        article_id=article.id,
        quiz_json=json.dumps(quiz_json)
    )

    db.add(quiz_record)
    db.commit()
    db.refresh(quiz_record)

    # 5️⃣ Return response
    return {
        "quiz_id": quiz_record.id,
        "title": article.title,
        "summary": article.summary,
        "quiz": quiz_json
    }


# -------------------------
# Get All Saved Quizzes (History Tab)
# -------------------------
@app.get("/quizzes")
def get_all_quizzes(db: Session = Depends(get_db)):
    quizzes = db.query(Quiz).order_by(Quiz.created_at.desc()).all()

    return [
        {
            "id": q.id,
            "article_id": q.article_id,
            "created_at": q.created_at
        }
        for q in quizzes
    ]

# -------------------------
# Get Single Quiz Details
# -------------------------
@app.get("/quizzes/{quiz_id}")
def get_quiz_details(quiz_id: int, db: Session = Depends(get_db)):
    quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()

    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")

    return {
        "id": quiz.id,
        "article_id": quiz.article_id,
        "quiz": json.loads(quiz.quiz_json),
        "created_at": quiz.created_at
    }
