import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def fcn():
    return question("What is your name?").reprompt("May I have your name?")


@ask.intent("MyNameIsIntent")

def name_fcn(firstname):
    msg = "Your name is {}".format(firstname)

    return statement(msg).simple_card("Hello {}". format(firstname) ,msg) 

@ask.intent("WhatIsMyNameIntent")
def fcn():
    return question("What is your name?")
if __name__ == '__main__':

    app.run(debug=True)