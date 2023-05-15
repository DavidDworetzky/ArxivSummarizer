from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY, LargeBinary, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from app.models.database.database import Base

class Article(Base):
    """
    Row used to represent an article entry in the database
    """
    __tablename__ = 'article'
    article_id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    author = Column(String)
    date = Column(DateTime)
    summary = Column(String)
    text = Column(String)
    embedding = Column(String)
