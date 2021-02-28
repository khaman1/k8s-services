from .shared import *

@app.route('/' + URL_PREFIX + '/time', methods = ['GET'])
async def get_time_from_external():
    retries = 25
    
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
            time.sleep(0.1)
    
    return 'Oops ...'