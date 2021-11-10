from flask import Flask, request, jsonify
from json_replies import responses

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>You've reached home</h1><p>This is a rest API server for Au10tix</p>"


@app.route('/test/all', methods=['GET'])
def get_companies():
    return jsonify(responses)


@app.route('/test/responses', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        req_id = int(request.args['id'])
    else:
        return "Error, check your code"

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for company in responses:
        if company['id'] == req_id:
            results.append(company)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)
