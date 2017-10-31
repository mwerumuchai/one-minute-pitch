from flask import render_template
from . import main
from ..models import Category
from .. import db

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    categories = Category.get_categories()
    title = 'Home - Welcome to One Minute Pitch'
    return render_template('index.html', title = title, categories = categories)

@main.route('/category/<int:id>')
def category(id):
    '''
    category route function returns a list of pitches chosen and allows users to create a new pitch
    '''
    category = Category.query.get(id)
    return render_template('category.html', title = title, category = category)

#Dynamic routing
@main.route('/pitch/<int:id>')
def pitch(id):
    '''
    view root page function that returns the pitch details page and its data
    '''
    title = f"Welcome to One Minute Pitch"
    return render_template('pitch.html', title = title, pitch = pitch)
