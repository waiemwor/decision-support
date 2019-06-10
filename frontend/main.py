from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/scenario/')
def scenario() :
	# List Scenes
	return render_template('scenario.html', variables={})

@app.route('/scenario/<name>')
def scenarioWithName(name) :
	# Query scene 
	# prooagate template
	# propagate all associate variables
	# save template and variables if needed.
	return render_template('scenario.html', name=name, variables={})

@app.route('/scenario/save')
def saveScene() :

	return 'OK'


@app.route('/scenario/test')
def scenarioTest() :
	return render_template('scenario.html', variables={ 'abc' : ['a', 'b', 'c', 'd'], 'aaaa' : ['x'] });