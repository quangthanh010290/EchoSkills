import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

from firebase import firebase

import time

firebase = firebase.FirebaseApplication('https://iotdev-6b58b.firebaseio.com', None)

app = Flask(__name__)

ask = Ask(app, "/")

#logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch

def launch():

    return question("Which room you want to turn off?")

@ask.intent("AnswerIntent")

def intent_fcn(roomName):
    msg = "Ligh on {} is turned off".format(roomName)
    if roomName == "kichen":
	print 'Light on kichen room is turned off'
    	firebase.put('/devices/8795002','status',False)
    if roomName == "living room":
	print 'Light on living room is turn off'
	firebase.put('/devices/390650','status',False)
    if roomName == 'bath':
	print 'Light on bath room is turn off'
	firebase.put('/rooms','bath_room',False)
    return statement(msg)

@ask.intent("AMAZON.YesIntent")
def yes_fcn(roomName):
    msg = "Ligh on {} is turned off".format(roomName)
    print roomName
    firebase.put('/123','states/001',False)
    return statement(msg)


def stop():
    return statement("Stoped")

if __name__ == '__main__':

    app.run(debug=False,host = '0.0.0.0', port=7000)
