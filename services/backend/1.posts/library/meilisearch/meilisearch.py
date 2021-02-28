import meilisearch

class Meilisearch:
    def __init__(self, index='books'):
        self.client = meilisearch.Client('http://meilisearch-srv:7700', 'meilisearch-dev')
        self.index  = self.client.index(index)
    
    def add(self, documents=''):
        if documents:
            if type(documents) == 'dict':
                self.index.add_documents([documents])
            else:
                self.index.add_documents(documents)
            
    def search(self, input=''):
        if type(input) == str:
            return self.index.search(input)