from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1= 3, number2= 8)

@app.route('/sum')
def number():
    x=5
    y=9
    return render_template('body.html', value1=x, value2=y, sum=x+y)

if __name__ == "__main__":
     app.run(host= '0.0.0.0', port=8081)  # for ec2 instances
     # app.run(debug=True, port=30000) # for localhost