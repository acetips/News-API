from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # bus_news = get_sources('business')
    # general_news = get_sources('general')
    # entertainment = get_sources('entertainment')
    title = "Home - Welcome to your number one news source"
    return render_template('index.html',title = title)

@app.route('/article/<article_id>')
def article(article_id):
    # article = get_articles(article_id)
    '''
    Wiew article page function that returns the article details page and its data
    '''
    return render_template('article.html', article = article)