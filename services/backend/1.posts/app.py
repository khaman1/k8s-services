import json
import time
from config.config import *
from config.extra import *
from endpoints.meilisearch import *
from endpoints.redis import *
from endpoints.worker_time import *




if __name__ == "__main__":
    app.run(host=HOST, port=PORT)