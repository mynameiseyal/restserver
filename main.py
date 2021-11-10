from flask import Flask, json

companies = [{"id": 1, "name": "Company One"}, {"id": 2, "name": "Company Two"}]

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return "<h1>You've reached home</h1><p>This is a rest API server for Au10tix</p>"


@app.route('/companies', methods=['GET'])
def get_companies():
  return json.dumps(companies)


if __name__ == '__main__':
    app.run()
