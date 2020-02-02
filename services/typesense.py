import typesense 
from secrets.config import api_key

class TypeSense:

    def __init__(self):
        super().__init__()
        self.client = typesense.Client({
            'master_node': {
                'host': '159.65.76.64',
                'port': '8108',
                'protocol': 'http',
                'api_key': api_key
            },
            'timeout_seconds': 2
        })
    
    def search(self, collection, search_params):
        return self.client.collections[collection].documents.search(search_params)
    
    def add_collection(self, schema):
        return self.client.collections.create(schema)
