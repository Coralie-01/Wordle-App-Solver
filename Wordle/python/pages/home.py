from flask import Blueprint, render_template

home = Blueprint('home',__name__)

@home.route('/home')
def wordle():
    return render_template('home.html')