from flask import render_template
from . import main

@main.route('/')
def index():

    title= 'Welcome to Myner Blog'
    return render_template('index.html', title = title)

@main.route('/about')
def about():
    tittle = 'About Myners Pitches'
    return render_template('about.html', tittle = tittle)