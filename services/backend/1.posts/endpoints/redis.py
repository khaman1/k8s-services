from .shared import *

async def get_hit_count():
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
async def check_visit():
    # return {
    #     'msg': 'Hello World'
    # }
    count = await get_hit_count()
    return 'Hello World! I have been seen {} times...\n'.format(count)