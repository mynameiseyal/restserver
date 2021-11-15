from rest_routes import app

"""
This is a simple rest API server, deployed using herokuapp.com
Base URL: https://au10restserver.herokuapp.com/
Example of usages:
1. https://au10restserver.herokuapp.com/api/all ==> returns all available responses JSONs 
2. https://au10restserver.herokuapp.com/api/responses ==> returns an error (no id is provided)
3. https://au10restserver.herokuapp.com/api/responses?serial=1 ==> returns the id=1 response as JSON
4. https://au10restserver.herokuapp.com/api/process & the correct JSON ==> returns correct if right, incorrect if not
"""

if __name__ == '__main__':
    app.run()
