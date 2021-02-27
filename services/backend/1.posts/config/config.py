import redis
from flask import Flask
from .vars import *

app = Flask(__name__)
cache = redis.Redis(host='redis-srv', port=6379)


from .init import *