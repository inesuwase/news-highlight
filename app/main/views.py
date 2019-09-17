
from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles
# Views
@main.route('/')
def index():
    '''
    View root page function that returns the category page and its data
    '''

    # Getting get source
    category_sources = get_sources('general')
    print(category_sources)
    title = 'Welcome to The resources of the news '
    return render_template('index.html', title = title, category_sources = category_sources)


# @main.route('/source/<id>')
# def Review(id):
# 	'''
# 	View Function that returns the news page and its data
# 	'''
# 	review = get_review(id)
#     # sources = get_sources(id)
# 	title = f'Top Articles'

# 	return render_template('source.html',title=title,review = review)   