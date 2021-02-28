from .shared import *
from library.meilisearch.meilisearch import Meilisearch

@app.route('/' + URL_PREFIX + '/document/add', methods = ['GET'])
async def add_document():    
    body = await request.form
    new_document = [{
        'id': body['id'],
        'title': body['title'],
        'poster': body['poster'],
        'overview': body['overview']
    }]
    
    print(new_document)

    Meilisearch().add(new_document)

    return "OK"
    
@app.route('/' + URL_PREFIX + '/document/search', methods = ['GET'])
async def search_document():
    text = request.args.get('text')
    
    print(text)
    
    result = Meilisearch().search(text)
    
    print(result)
    
    return result