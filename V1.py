#from bottle import route, run

from sys import argv

from bottle import *

@route("/")
def index():
    return """
    <h2>Verkefni 2</h1>
    
    """

#run(host="localhost", port=8080, debug=True)

bottle.run(host='0.0.0.0',port=argv[1])


 
@route("/")
def index():
    return """
    <h2>Verkefnki 1</h1>
    <a href="/about">About</a>
    <a href="/bio">Bio</a>
    <a href="/pic">Pictures</a>
"""

@route("/about")
def elvar():
    return "Hér er sögn um mig"

@route("/bio")
def elvar():
    return"Hér er Biograph"

@route("/pic")
def elvar():
    return "Hér er ljósmynd"

#run(host="localhost", port=8080, debug=True)
