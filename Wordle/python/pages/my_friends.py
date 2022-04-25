from flask import Flask, Blueprint, render_template, session, request, redirect,url_for
import sqlite3
from python.functions.search import liste_users_minus_friends, recherche
from python.functions.friends import ajoute, liste_amis
from python.functions.classement import classe_amis
from python.functions.is_connected import test_login

my_friends = Blueprint('my_friends',__name__)

@my_friends.route('/my_friends')
def show_friends():
    if test_login :
        user = str(session.get("name"))
        l = classe_amis(user)
        n = len(l)
        return render_template('my_friends.html',data=l,n=n)
    else:
        return redirect('/login')


@my_friends.route('/my_friends/add',)
def search_friends():
    if test_login :
        return render_template('add_friends.html')
    else:
        return redirect('/login')

@my_friends.route('/my_friends/add',methods=['POST'])
def add_friends():
    if test_login:
        search = request.form.get('search')
        user = session.get('name')
        l = liste_users_minus_friends(user)
        l.remove((user,))
        users_found = recherche(search,l)
        empty = (users_found==[])
        return render_template('add_friends.html',users_found=users_found,empty=empty)
    else:
        return redirect('/login')


@my_friends.route('/ajouter/<user>')
def add(user):
    if test_login:
        user1,user2 = session.get('name'),user
        ajoute(user1,user2)
        return redirect(url_for('my_friends.add_friends'))
    else:
        return redirect('/login')