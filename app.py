from datetime import datetime
from genericpath import exists
from importlib.resources import path
from itertools import count
from operator import truediv
import shutil
from flask import Flask, render_template
from os import listdir, path
import os
import zipfile
import io
import sqlite3
import secretKeys
import config as config
import requests

app = Flask(__name__)
destinyAPIRoot = 'https://www.bungie.net/Platform/Destiny2'
destinyManifestRoot = 'https://www.bungie.net/'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/manifest')
def manifest():
	responseManifest = gatherDestintyManifest()
	return render_template('manifest.html', manifest=responseManifest)

@app.route('/strikes')
def strikes():
	HEADERS = {"X-API-Key": secretKeys.X_API_Key}
	response = requests.get(f'{destinyAPIRoot}/Milestones/', headers=HEADERS)
	strikes_endpoint = response.json()['Response']['1942283261']['activities']
	print (strikes_endpoint)
	return render_template('strikes.html',strikes=strikes_endpoint)

def gatherDestintyManifest():
	# If the manifest folder has not been initialized 
	# OR it has been initialized but there is no manifest document inside it
	# OR there is a manifest file but it is old (destiny reset at 10am every day)
	if (not os.path.exists(config.MANIFEST_FOLDER) or
	 	not os.path.listdir(config.MANIFEST_FOLDER).count == 1 or
	 	os.path.getmtime(os.path.listdir(config.MANIFEST_FOLDER)[0]) < datetime(day=datetime.today, hour=10)):
		
		HEADERS = {"X-API-Key": secretKeys.X_API_Key}
		response = requests.get(f'{destinyAPIRoot}/Manifest/')
		responseManifest = response.json()['Response']
		mobileAssetContentPath = responseManifest['mobileAssetContentPath']
		
		sqlitePath = f'{destinyManifestRoot}{mobileAssetContentPath}'
		sqliteZip = requests.get(sqlitePath, stream=True)
		
		# If the folder exists delete it and anything in it.
		if (os.path.exists(config.MANIFEST_FOLDER)):
			shutil.rmtree(config.MANIFEST_FOLDER)

		z = zipfile.ZipFile(io.BytesIO(sqliteZip.content))
		z.extractall('DestinyManifest')

		return responseManifest
