from asyncio.windows_events import NULL
from flask import Flask, render_template
import config
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


def request_postmasterContents():
	return NULL
