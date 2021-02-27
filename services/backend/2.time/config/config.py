import os
from flask import Flask

app = Flask(__name__)

#################################
#################################
APP_VERSION = os.environ['APP_VERSION']
URL_PREFIX  = os.environ['URL_PREFIX']


#################################
#################################
from .init import *