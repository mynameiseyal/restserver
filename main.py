from rest_routes import app

"""
This is a simple rest API server, deployed using herokuapp.com
Base URL: https://au10restserver.herokuapp.com/
Example of usages:
1. https://au10restserver.herokuapp.com/test/all ==> returns all available responses JSONs 
2. https://au10restserver.herokuapp.com/test/responses ==> returns an error (no id is provided)
2. https://au10restserver.herokuapp.com/test/responses?id=1 ==> returns the id=1 response as JSON
"""

if __name__ == '__main__':
    app.run()
