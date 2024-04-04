#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

# the decorator are functions that takes func argumrnts and return them decorated with new features.

# Anything included in the route passed to the app.route decorator with angle brackets <> will be passed to the decorated func as param.

# we can make sure that the user is a valid string by modifying user as below.

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)