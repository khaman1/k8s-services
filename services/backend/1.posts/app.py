import json
import time
import requests
from config.config import *
from config.extra import *

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/' + URL_PREFIX, methods = ['GET'])
def check_visit():
    # return {
    #     'msg': 'Hello World'
    # }
    count = get_hit_count()
    return 'Hello World! I have been seen {} times...\n'.format(count)


@app.route('/' + URL_PREFIX + '/time', methods = ['GET'])
def get_time_from_external():
    retries = 5
    
    time_input_queue.sendMessage(delay=0).message(json.dumps({'msg':'Hello World'})).execute()
    
    while retries > 0:
        try:
            msg = time_output_queue.receiveMessage().execute()
            msg['message'] = json.loads(msg['message'])
            
            # Delete Message
            time_output_queue.deleteMessage(id=msg['id']).execute()
            
            return msg
        except:
            retries -= 1
            time.sleep(0.5)
    
    return 'Oops ...'