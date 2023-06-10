#jinja2 template engine
'''
{%...%}   conditions,for loop
{{ }}    expresions to print output
{#....#} this is for comments
'''


from flask import Flask, redirect, url_for, render_template,request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
   res=''
   if score >= 50:
       res='pass'
   else:
       res='fail'
   
   exp={'score':score,'result':res}
   return render_template('result.html', result=exp)     #--forloop statement
   #return render_template('result.html', result=score)  #--if else statement
    
@app.route('/fail/<int:score>')
def fail(score):
    if score < 50:
        return "The Person has failed and the marks is " + str(score)

### Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks >= 50:
        result = 'success'
    else:
        result = 'fail'

    return redirect(url_for(result, score=marks))

# Result checker submit HTML page 
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_marks = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_marks = science + maths + c + datascience
    
    return redirect(url_for('success', score=total_marks))


if __name__ == '__main__':
    app.run(debug=True)