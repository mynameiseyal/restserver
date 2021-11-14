import json
from types import SimpleNamespace

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
    if 'serial' in request.args:
        req_id = int(request.args['serial'])
    else:
        return "Error, check your code"

    results = []
    for resp in responses:
        if resp['serial'] == req_id:
            results.append(resp)

    return jsonify(results)


@app.route('/api/process', methods=['GET', 'POST'])
def process_responses():
    """
    Gets a rest API call containing a JSON.
    Expected JSON: {"message": {"subset":[{"general":{
                    "information": {"date": "1-2-2021","version": "3.00"},
                    "quantities": {"first": "203.70","second": "104.4","third": "150"}}}]},
                    "serial": 3}
    :return: Correct if right, Incorrect if not
    """
    content = request.get_json()
    parsed = json.loads(content, object_hook=lambda d: SimpleNamespace(**d))
    print(content)
    if parsed.serial == 3:
        if content['message']['subset'][0]['general']['information']['date'] == '1-2-2021':
            if content['message']['subset'][0]['general']['information']['version'] == '3.00':
                if content['message']['subset'][0]['general']['quantities']['first'] == '203.70':
                    if content['message']['subset'][0]['general']['quantities']['second'] == '104.4':
                        if content['message']['subset'][0]['general']['quantities']['third'] == '150':
                            return "Correct"
                        else:
                            return "Incorrect"
