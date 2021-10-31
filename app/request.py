from app import app
import urllib.request,json

from app.article_test import Article
from .models import article

Article = article.Article

# Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the artile base url
base_url = app.config['ARTICLE_API_BASE_URL']

def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        article_results =None

        if get_articles_response['results']:
            article_results_list = get_articles_response['results']
            article_results = process_results(article_results_list)

    return article_results

def process_results(article_list):
    '''
    Function that processes the article result and transform them to a list of objects
    '''
    article_results = []
    for article_item in article_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        if urlToImage:
            article_object = Article(author,title,description,url,urlToImage,publishedAt,content)
            article_results.append(article_object)

    return article_results
