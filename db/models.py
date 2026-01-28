from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from db.database import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(Text, unique=True, nullable=False)
    title = Column(Text, nullable=False)
    summary = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    quizzes = relationship("Quiz", back_populates="article")


class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey("articles.id"), nullable=False)

    quiz_json = Column(Text, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    article = relationship("Article", back_populates="quizzes")


