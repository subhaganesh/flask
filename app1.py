from flask import Flask

# Create a Flask application(wsgi application)
app = Flask(__name__)

# Define a route and its corresponding view
@app.route('/')
def welcome():
    return 'Hi i am subhaganesh. i am a machine learning engineer'

@app.route('/skills')
def skills():
    return '''python,
              pandas,
              matplotlib,
              sql,
              power bi,
              web scraping,
              machine learning'''

# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)

