#!/usr/bin/env python3
""" Basic Babel setup """
from flask_babel import Babel, gettext
from flask import Flask, render_template, request, g
import pytz
import datetime

app = Flask(__name__)
babel = Babel(app)

"""user table"""
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """class for configuring language and default timezone"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def root():
    """returns template index.html"""
    return render_template("index.html")


@babel.localeselector
def get_locale():
    """determines the best match with our supported languages"""
    local_lang = request.args.get('locale')
    supported_lang = app.config['LANGUAGES']
    if local_lang in supported_lang:
        return local_lang
    userId = request.args.get('login_as')
    if userId:
        local_lang = users[int(userId)]['locale']
        if local_lang in supported_lang:
            return local_lang
    local_lang = request.headers.get('locale')
    if local_lang in supported_lang:
        return local_lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """
    returns a user dictionary or None if the ID cannot
    be found or if login_as was not passed
    """
    try:
        userId = request.args.get('login_as')
        return users[int(userId)]
    except Exception:
        return None


@app.before_request
def before_request():
    """
    use get_user to find a user if any,
    and set it as a global on flask.g.user
    """
    g.user = get_user()
    utcNow = pytz.utc.localize(datetime.datetime.utcnow())
    local_time_now = utcNow.astimezone(pytz.timezone(get_timezone()))


@babel.timezoneselector
def get_timezone():
    """Infer appropriate time zone"""
    localTimezone = request.args.get('timezone')
    if localTimezone:
        if localTimezone in pytz.all_timezones:
            return localTimezone
        else:
            raise pytz.exceptions.UnknownTimeZoneError
    try:
        userId = request.args.get('login_as')
        user = users[int(userId)]
        localTimezone = user['timezone']
    except Exception:
        localTimezone = None
    if localTimezone:
        if localTimezone in pytz.all_timezones:
            return localTimezone
        else:
            raise pytz.exceptions.UnknownTimeZoneError
    return app.config['BABEL_DEFAULT_TIMEZONE']


if __name__ == "__main__":
    app.run()
