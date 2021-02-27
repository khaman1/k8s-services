from .config import *

@app.route('/', methods = ['GET'])
def hello():
    return "Service: " + URL_PREFIX

@app.route('/' + URL_PREFIX + '/version', methods = ['GET'])
def app_version():
    return APP_VERSION