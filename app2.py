#building url dynamically
#variable rules & url building

from flask import Flask

app = Flask(__name__)

@app.route('/')
def intro():
    return 'Welcome to my page'

@app.route('/tool1/<talent1>')
def role1(talent1):
    if talent1 == 'python':
        return 'Python developer will write readable code'
    else:
        return 'Invalid talent1'

@app.route('/tool2/<talent2>')
def role2(talent2):
    if talent2 == 'ml_eng':
        return 'Will be good at algorithms'
    else:
        return 'Invalid talent2'

@app.route('/tool3/<talent3>')
def role3(talent3):
    if talent3 == 'data_scientist':
        return 'Good at algo and decision making'
    else:
        return 'Invalid talent3'

@app.route('/skill/<result>')
def skill(result):
    if result == 'python':
        return role1('python')
    elif result == 'ml_eng':
        return role2('ml_eng')
    elif result == 'data_scientist':
        return role3('data_scientist')
    else:
        return 'Invalid skill'

# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
