import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

from firebase import firebase

import time

firebase = firebase.FirebaseApplication('https://iotdev-6b58b.firebaseio.com', None)

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch

def launch():

    return question("Which room you want to turn on?")

@ask.intent("AnswerIntent")

def intent_fcn(roomName):
    msg = "Ligh on {} is turned off".format(roomName)
    if roomName == "kichen":
        print 'Light on kichen room is turned off'
        firebase.put('/rooms','kichen_room',True)
    if roomName == "living":
        print 'Light on living room is turn off'
        firebase.put('/rooms','living_room',True)
    if roomName == 'bath':
        print 'Light on bath room is turn off'
        firebase.put('/rooms','bath_room',True)
    return statement(msg)
@ask.intent("AMAZON.YesIntent")
def yes_fcn(roomName):
    msg = "Ligh on {} is turned on".format(roomName)
    firebase.put('/123','states/001',True)
    return statement(msg)


def stop():
    return statement("Stoped")

if __name__ == '__main__':

    app.run(debug=True,host = '0.0.0.0', port=6000)
