import functools
from flask import flash, redirect, url_for, session


def requires_login(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not session.get('email'):
            flash("you need to sign in for this page", "danger")
            return redirect(url_for("home"))
        return func(*args, **kwargs)
    return inner
