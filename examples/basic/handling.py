import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch

def launch():

    return statement("Welcome to request demo")

@ask.intent("HelloIntent")

def intent_fcn():
    return question("Do you want to stop?")

@ask.intent("AMAZON.StopIntent")

def stop():
    return statement("Stoped")


if __name__ == '__main__':

    app.run(debug=True)