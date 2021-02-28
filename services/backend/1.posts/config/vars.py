import os

# APP_VERSION = 0.01
# URL_PREFIX  = 'posts'
# DELAY       = 1
# TIMEOUT     = 5

HOST        = os.environ['HOST']
PORT        = os.environ['PORT']
APP_VERSION = os.environ['APP_VERSION']
URL_PREFIX  = os.environ['URL_PREFIX']
DELAY       = float(os.environ['DELAY'])
TIMEOUT     = float(os.environ['TIMEOUT'])