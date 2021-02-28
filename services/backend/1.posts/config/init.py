from .config import *

@app.route('/', methods = ['GET'])
async def hello():
    return "Service: " + URL_PREFIX

@app.route('/' + URL_PREFIX + '/version', methods = ['GET'])
async def app_version():
    return str(APP_VERSION)