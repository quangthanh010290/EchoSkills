import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch

def launch():

    return question("Which room you want to turn on?")

@ask.intent("AnswerIntent")

def intent_fcn(roomName):
    msg = "Please Confirm that you wan to turn on the {} light on".format(roomName)
    return question(msg)

@ask.intent("AMAZON.YesIntent")
def yes_fcn(roomName):
    msg = "Ligh on {} is turned on".format(roomName)
    return statement(msg)


def stop():
    return statement("Stoped")

if __name__ == '__main__':

    app.run(debug=True)