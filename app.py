from flask import Flask
from flask import jsonify
from flask import request
from services.typesense import TypeSense
app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    healthy = {'success' : True}
    return jsonify(healthy), 200

@app.route('/search/', methods=['POST'])
def search():
    data = request.get_json()
    search_params = data['search_params']
    collection = data['collection']
    # search_parameters = {
    #     'q'         : 'harry',
    #     'query_by'  : 'title',
    #     'sort_by'   : 'ratings_count:desc'
    # }
    print(search_params)
    print(collection)
    result = client.search(collection, search_params)

    return jsonify(result), 200

@app.route('/create/collection', methods=['POST'])
def create_collection():
    result = client.create_collection(schema)
    return jsonify(result), 200

@app.route('')

if __name__ == '__main__':
    client = TypeSense()
    app.run()