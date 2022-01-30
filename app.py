from flask import Flask, render_template
import sqlite3
import secrets
import requests

app = Flask(__name__)
destinyAPIRoot = 'https://www.bungie.net/Platform/Destiny2'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/manifest')
def manifest():
	HEADERS = {"X-API-Key": secrets.X_API_Key}
	response = requests.get(f'{destinyAPIRoot}/Manifest/')
	responseManifest = response.json()['Response']
	print(responseManifest)
	return render_template('manifest.html', manifest=responseManifest)

@app.route('/strikes')
def strikes():
	HEADERS = {"X-API-Key": secrets.X_API_Key}
	response = requests.get(f'{destinyAPIRoot}/Milestones/', headers=HEADERS)
	strikes_endpoint = response.json()['Response']['1942283261']['activities']
	print (strikes_endpoint)
	return render_template('strikes.html',strikes=strikes_endpoint)