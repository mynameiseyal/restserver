from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'title1',
        'description': u'artifact1',
        'done': False
    },
    {
        'id': 2,
        'title': u'title2',
        'description': u'artifact2',
        'done': False
    }
]


def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)
