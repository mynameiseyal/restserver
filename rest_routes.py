import json
import time
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
    Expected JSON: {"message": {"subset":{"general":{
                    "information": {"date": "1-2-2021","version": "3.00"},
                    "quantities": {"first": "203.70","second": "104.4","third": "150"}}}},
                    "serial": 3}
    :return: Correct if right, Incorrect if not
    """
    content = request.get_json()
    parsed = json.loads(json.dumps(content), object_hook=lambda d: SimpleNamespace(**d))
    if parsed.serial == 3 and\
            parsed.message.subset.general.information.date == '1-2-2021' and\
            parsed.message.subset.general.information.version == '3.00' and\
            parsed.message.subset.general.quantities.first == '203.70' and\
            parsed.message.subset.general.quantities.second == '104.4' and \
            parsed.message.subset.general.quantities.third == '150':
        return "Correct"
    else:
        return "Incorrect"


@app.route('/RestServer/sleep', methods=['GET', 'POST'])
def sleep():
    """
    Provides a timeout according to a seconds value
    Exmaple: /sleep?sleep_time=10
    """
    sleep_time = request.args.get('sleep_time')
    time.sleep(int(sleep_time))
    return '', 200
