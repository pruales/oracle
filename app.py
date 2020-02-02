from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    healthy = {'success' : True}
    return jsonify(healthy), 200



if __name__ == '__main__':
app.run()