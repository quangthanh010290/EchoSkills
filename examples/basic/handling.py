import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch

def launch():

    return statement("Welcome to the request demo, this is launch request")

@ask.intent("HelloIntent")

def intent_fcn():
    return statement("This is handler of hello intent")



if __name__ == '__main__':

    app.run(debug=True)