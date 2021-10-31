from app import app
import urllib.request,json

from app.article_test import Article
from .models import article

Article = article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the artile base url
base_url = app.config['ARTICLE_API_BASE_URL']