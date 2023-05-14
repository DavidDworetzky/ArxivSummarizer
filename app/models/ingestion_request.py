from dataclasses import dataclass
from typing import Array

@dataclass
class IngestionRequest:
    article_urls: Array[str]
