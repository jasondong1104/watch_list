from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/home')
def hello():
    return '<h1>欢迎来到 My Watchlist!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page(name):
    return f'Hello, {escape(name)}'
