import json
import logging
import os
import requests

from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

GITHUB_USERNAME = os.environ.get('GITHUB_USERNAME')
GITHUB_PASSWORD = os.environ.get('GITHUB_PASSWORD')

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/update/lights/effect', methods=['POST'])
def update_lights_effect_request():
    effect_name = request.args.get('name')
    make_github_issue("LightUpdate|Effect|" + effect_name)
    return effect_name

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

# https://gist.github.com/JeffPaine/3145490
def make_github_issue(title):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/AndrewDorm/Public/issues'
    # Create an authenticated session to create the issue
    session = requests.Session()

    session.auth = (GITHUB_USERNAME, GITHUB_PASSWORD)
    # Create our issue
    issue = {'title': title}
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print ('Successfully created Issue {0:s}'.format(title))
    else:
        print ('Could not create Issue {0:s}'.format(title))
        print ('Response:', r.content)

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
