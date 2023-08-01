#!/usr/bin/env python3
""" Basic Babel setup """
from flask_babel import Babel
from flask import Flask, render_template, request

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """class for configuring language and default timezone"""
    LANGUAGES = ['en', 'fr']
    DEFAULT_LOCALE = 'en'
    DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def root():
    """returns template 2-index.html"""
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    """determines the best match with our supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
