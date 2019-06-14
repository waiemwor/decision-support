from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
	# hello world test page.
    return 'Hello, World!'


@app.route('/scenario/')
def scenario() :
	'''
	Show blank scenario page
	'''
	return render_template('scenario.html', variables={})

@app.route('/scenario/<name>')
def scenarioWithName(name) :
	'''
	scenario.html template can receive "name" and "template", "variables" as parameters.
	These parameters will be propagataed to the template.
	'''
	return render_template('scenario.html', name=name, template='', variables={})

@app.route('/scenario/save')
def saveScene() :
	'''
	Placeholder for implementing save feature.
	'''
	return 'OK'


@app.route('/scenario/test')
def scenarioTest() :
	'''
	Test page
	'''
	temp = 'You are working on your laptop using ${NetworkType}. You will need a password that ${Password}'
	return render_template('scenario.html', name='Test scenario', 
											template=temp, 
											variables={ 'NetworkType' : ['Public Wifi', 'VPN-Unencrypted', 'VPN-Encrypted', 'Private-Network'], 
														'Password' : ['Weak', 'Strong'] 
													  });