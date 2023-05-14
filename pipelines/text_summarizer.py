#text summarizer abstract base class
from abc import ABC, abstractmethod
from typing import Optional
import requests
from lxml import etree
from app.models.database import article
from app.models.database.database import Session

class TextSummarizer(ABC):
    """
    Abstract base class for text summarizer models
    """
    @abstractmethod
    def summarize(self, text) -> str:
        """
        Summarize the given text
        :param text: text to summarize
        :return: summary of the text
        """
        pass

    @abstractmethod
    def generate_embedding(self, text) -> str:
        """
        Generate an embedding for the given text
        :param text: text to generate embedding for
        :return: embedding of the text
        """
        pass

    def crawl_article(self, url) -> article.Article:
        """
        Crawl the given article and return the text
        :param url: url of the article to crawl
        :return: text of the article
        """
        #make an http request to the arxiv url
        response = requests.get(url)
        #extract the title by looking for <class="title mathjax"> and </h1>
        #extract the author by looking for <meta name="citation_author" content="
        #extract the date by looking for <meta name="citation_date" content="
        #extract the summary by looking for <blockquote class="abstract mathjax"> and </blockquote>
        #extract the text by looking for <div class="full-text"> and </div>
        text = response.content
        parser = etree.HTMLParser()
        tree = etree.fromstring(text, parser)
        title_xpath = '//title/text()'
        title = tree.xpath(title_xpath)
        author_xpath = '//meta[@name="citation_author"]/@content'
        author = tree.xpath(author_xpath)
        date_xpath = '//meta[@name="citation_date"]/@content'
        date = tree.xpath(date_xpath)
        summary_xpath = '//blockquote[@class="abstract mathjax"]/text()'
        summary = tree.xpath(summary_xpath)
        text_xpath = '//div[@class="full-text"]/text()'
        article_text = tree.xpath(text_xpath)

        #now, create an article model and persist it to the database
        #create an article model
        article_model = article.Article(title=title, url=url, author=author, date=date, summary=summary, text=article_text)
        #persist the article model to the database
        Session.add(article_model)
        Session.commit()
        #return the article model
        return article_model