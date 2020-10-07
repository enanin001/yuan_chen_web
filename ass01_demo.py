

# A very simple Bottle Hello World app for you to get started with...
import os
from bottle import default_app, route, template, run

ON_PYTHONANYWHERE = "PYTHONANYWHERE_DOMAIN" in os.environ.keys()

if ON_PYTHONANYWHERE:
    from bottle import default_app
else:
    from bottle import run, debug

@route('/')
def link_color():
    return template("link_color")

@route ('/color_bar')
def color_bar():
    return template("color_bar")


if ON_PYTHONANYWHERE:
    application = default_app()
else:
    debug(True)
    run(host="localhost", port=8080)