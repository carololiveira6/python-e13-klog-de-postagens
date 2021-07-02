from flask import Flask


def init_app(app: Flask):
    from .posts_view import bp as bp_form

    app.register_blueprint(bp_form)