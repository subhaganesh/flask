### Building Url Dynamically 
####Variable Rules And URL Building

from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my Youtube Channel'

@app.route('/success/<int:score>')
def success(score):
    if score>=50:
       return "The Person has passed and the marks is "+ str(score)

    
@app.route('/fail/<int:score>')
def fail(score):
    if score<50:
        return "The Person has failed and the marks is "+ str(score)


### Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks>=50:
        result='success'
    else:
        result='fail'

    return redirect(url_for(result,score=marks))


if __name__=='__main__':
    app.run(debug=True)