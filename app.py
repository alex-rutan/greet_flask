from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def welcome_user():
    """Returns simple "welcome" greeting"""

    return "welcome"


@app.route('/welcome/home')
def welcome_user_home():
    """Returns simple "welcome home" greeting"""

    return "welcome home"


@app.route('/welcome/back')
def welcome_user_backl():
    """Returns simple "welcome back" greeting"""

    return "welcome back"