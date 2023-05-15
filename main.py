#framework
import sys
from typing import Optional
from app.models.database import article
from app.models.ingestion_request import IngestionRequest
from pipelines.text_summarizer_gpt4 import TextSummarizerGPT4
import logging
from fastapi import FastAPI, Depends, HTTPException
from dotenv import load_dotenv
import os
from app.models.database.database import Session

load_dotenv()
openai_key = os.getenv("OPENAI_TOKEN")

#constants
api_version = 0.1
enhanced_logging = False

if enhanced_logging:
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


#initialization
app = FastAPI()

#routes
@app.get("/")
def version():
    return {"version": api_version}

@app.post("/ingest_articles")
def ingest_articles(params: IngestionRequest):
    """
    Ingest articles from arxiv
    """
    summarizer = TextSummarizerGPT4(openai_key)
    for url in params.article_urls:
        article_model = summarizer.crawl_article(url)
        summary = summarizer.summarize(article_model.text)
        embedding = summarizer.generate_embedding(article_model.text)
        article_model.summary = summary
        article_model.embedding = embedding
        Session.commit()


#article endpoint with optional query parameter of number of articles
@app.get("/article/{article_count}")
def article(article_count: int = 1):
    """
    Gets a number of articles from the database
    """
    return article.Article.query.limit(article_count).all()
    