from flask import Flask, render_template
import sqlite3
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
	HEADERS = {"X-API-Key": secrets.X_API_Key}
	response = requests.get('https://www.bungie.net/Platform/Destiny2/Manifest/')
	textToPrint = response.json()['Response']
	print(textToPrint)
	return render_template('manifest.html', manifest=textToPrint)

@app.route('/strikes')
def strikes():
	HEADERS = {"X-API-Key": secrets.X_API_Key}
	response = requests.get('https://www.bungie.net/Platform/Destiny2/Milestones/', headers=HEADERS)
	nightfall_endpoint = response.json()['Response']['1942283261']['activities']
	print (nightfall_endpoint)
	return render_template('manifest.html',manifest=nightfall_endpoint)