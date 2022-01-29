from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/manifest')
def manifest():
	HEADERS = {"X-API-Key":'MY-X-API-Key'}
	response = requests.get('https://www.bungie.net/Platform/Destiny2/Manifest/', headers=HEADERS)
	return response.json()