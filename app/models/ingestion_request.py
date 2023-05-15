from dataclasses import dataclass
from typing import Any, List
from pydantic import BaseModel

class IngestionRequest(BaseModel):
    article_urls: List[str]
