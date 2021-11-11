from flask import Flask, request, jsonify
from json_replies import responses

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """
    :return: Home message
    """
    return "<h1>You've reached home</h1><p>This is a rest API server for Au10tix</p>"


@app.route('/api/all', methods=['GET'])
def get_responses():
    """
    :return: all responses
    """
    return jsonify(responses)


@app.route('/api/responses', methods=['GET'])
def api_id():
    """
    Checks if the args contains an id of the response
    :return: response according to id or error message
    """
    if 'id' in request.args:
        req_id = int(request.args['id'])
    else:
        return "Error, check your code"

    results = []
    for resp in responses:
        if resp['id'] == req_id:
            results.append(resp)

    return jsonify(results)


@app.route('/api/add_message/<uuid>', methods=['GET', 'POST'])
def add_message(uuid):
    content = request.get_json()
    return content
