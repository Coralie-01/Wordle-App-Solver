from audioop import add
from flask import Flask

def App():
    app = Flask(__name__)
    from python.pages.home import home
    from python.pages.Jeu import game
    from python.pages.Search import search
    from python.pages.authentification import authentification
    from python.pages.login import login
    from python.pages.stats import stats
    from python.pages.play import games
    from python.pages.add_friend import add_friend
    from python.pages.my_account import my_account


    app.register_blueprint(games)
    app.register_blueprint(home)
    app.register_blueprint(game)
    app.register_blueprint(search)
    app.register_blueprint(authentification)
    app.register_blueprint(login)
    app.register_blueprint(stats)
    app.register_blueprint(add_friend)
    app.register_blueprint(my_account)


    return app

if __name__ == "__main__":
    app = App()
    app.run(debug=1)