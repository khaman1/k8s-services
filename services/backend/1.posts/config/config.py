import redis
from quart import Quart, render_template, websocket
from .vars import *

app = Quart(__name__)
cache = redis.Redis(host='redis-srv', port=6379)

from .init import *