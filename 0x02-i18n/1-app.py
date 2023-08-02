#!/usr/bin/env python3
""" Basic Babel setup """
from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """class for configuring language and default timezone"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def root():
    """returns template 1-index.html"""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
