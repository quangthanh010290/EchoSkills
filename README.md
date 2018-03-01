# Install packagets
apt-cache search libssl | grep SSL

sudo apt-get install libssl-dev

sudo apt-get install libssl-ocaml

sudo apt-get install libssl-ocaml-dev

sudo apt-get install libffi-dev
 
sudo pip install flask-ask


# Tutorial 
https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development

# Ngrok Tool
https://ngrok.com/download
To start a HTTP tunnel on port 80

`./ngrok http 80`
# Git
https://github.com/johnwheeler/flask-ask
# Elexa Development Page
https://developer.amazon.com/home.html

#Getting Started With Alexa Development skill kit
https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/getting-started-guide

# Run the App

1. Run ngrok on specific port 

2. Edit the code to ensure they have same port 

`app.run(debug=True,host = '0.0.0.0', port=6000)`
