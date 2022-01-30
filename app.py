from distutils.command import config
import secrets
from flask import Flask, render_template
import secrets
import requests

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/manifest')
def manifest():
	HEADERS = {"X-API-Key":'0ee4d3d2c37241cab72adef18a885b43'}
	response = requests.get('https://www.bungie.net/Platform/Destiny2/Manifest/')
	textToPrint = response.json()['Response']
	print(textToPrint)
	return render_template('manifest.html', manifest=textToPrint)