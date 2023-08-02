#!/usr/bin/env python3
""" Basic Babel setup """
from flask_babel import Babel, gettext
from flask import Flask, render_template, request

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
    """returns template 4-index.html"""
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """determines the best match with our supported languages"""
    local_lang = request.args.get('locale')
    supported_lang = app.config['LANGUAGES']
    if local_lang in supported_lang:
        return local_lang
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
