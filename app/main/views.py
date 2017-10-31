from flask import render_template
from . import main
from ..models import Category, User,Peptalk
from .. import db
from flask_login import login_required

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
    categories = Category.query.get(id)
    pitches = Peptalk.get_pitches(id)
    title = "Pitches"
    return render_template('category.html', title = title, categories = categories,pitches = pitches)

# Dynamic routing
@main.route('/category/pitch/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_pitch(id):
    '''
    Function to check Pitches form
    '''
    form = PeptalkForm()
    category = Category.query.filter_by(id=id).first()

    if form.validate_on_submit():
        pitch = form.pitch.data
        user = current_user._get_current_object()
        new_pitch = Peptalk(category_id=Category.id,content=content, user_id=user.id)
        new_pitch.save_pitch()
        return redirect(url_for('.category', id = category.id))

    title = f'{category.title} pitch'
    return render_template('pitch.html', title = title, pitch_form = pitch, category=category)
