#building url dynamically
#variable rules & url building

from flask import Flask,redirect,url_for

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

@app.route('/skill/<input>')
def skill(input):
    if input == 'python':
        result= 'role1'
    elif input == 'ml_eng':
        result= 'role2'
    elif input == 'data_scientist':
        result= 'role3'
    else:
        result ='Invalid skill'

    return redirect(url_for(result,talent1=input,talent2=input,talent3=input))

# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
