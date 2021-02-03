
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import math





app = Flask(__name__)




@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
@app.route('/home')
def main():
    return render_template("index.html")


@app.route('/calculator')
def calculator():
    return render_template("calculator.html")


@app.route('/calculate', methods=['POST'])
def calculate(sum=sum):
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']
        if operation == 'plus':
            sum = float(num1)+float(num2)
            return render_template("calculator.html", sum=sum)
        if operation == 'minus':
            sum = float(num1)-float(num2)
            return render_template("calculator.html", sum=sum)
        if operation == 'multiply':
            sum = float(num1)*float(num2)
            return render_template("calculator.html", sum=sum)
        if operation == 'divide':
            sum = float(num1)/float(num2)
            return render_template("calculator.html", sum=sum)


@app.route('/GDZ')
def gdz():
    return render_template("gdz.html")


@app.route('/discriminant')
def discriminant():
    return render_template("discriminant.html")


@app.route('/disresult', methods=['POST'])
def disresult(sum=sum):
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        c = request.form['c']

        sum = float(b)*float(b)-4*float(a)*float(c)
        return render_template("discriminant.html", sum=sum)


@app.route('/square_equations')
def equations():
    return render_template("square-equations.html")


@app.route('/sqrt_of_equations', methods=['POST'])
def sqrt(sum=sum):
    if request.method == 'POST':
     a = float(request.form['a'])
     b = float(request.form['b'])
     c = float(request.form['c'])
     discriminant = (b ** 2) - (4 * a * c)
     if discriminant < 0:
         sum = "Нет решений"
     elif discriminant > 0:
         sqrtofdis = math.sqrt(discriminant)
         x1 = ((-b) + sqrtofdis)/(2*a)
         x2 = ((-b) - sqrtofdis)/(2*a)
         sum = x1,x2
     elif discriminant == 0:
        # sqrtofdis = math.sqrt(discriminant)
         x = (-b)/(2*a)
         sum = x

     return render_template("square-equations.html", sum=sum)


@app.route('/sqrt')
def sqrtofnum():
    return render_template("sqrt.html")


@app.route('/sqrtsend', methods=['POST'])
def sqrtofnumber(sum=sum):

    if request.method == 'POST':
        num = float(request.form['num'])
        sum = math.sqrt(num)
        return render_template("sqrt.html", sum=sum)


@app.route('/converter')
def convert():
    return render_template("converter.html")


@app.route('/temp')
def temp():
    return render_template("temp.html")


@app.route('/temp_send', methods=['POST'])
def temp_send(sum=sum):
    if request.method == 'POST':
        num = float(request.form['num'])
        convert = request.form['convert']
        if convert == "Farengeit-to-Celci":
            sum = (num - 32)*5/9
            return render_template("temp.html", sum=sum)
        elif convert == "Celci-to-Farengeit":
            sum = (num*9/5)+32
            return render_template("temp.html", sum=sum)
        elif convert == "Celvin-to-Celci":
            sum = num-273.15
            return render_template("temp.html", sum=sum)
        elif convert == "Celci-to-Celvin":
            sum = num+273.15
            return render_template("temp.html", sum=sum)
        elif convert == "Celvin-to-Farengeit":
            sum = (num-273.15)*9/5+32
            return render_template("temp.html", sum=sum)
        elif convert == "Farengeit-to-Celvin":
            sum = (num-32)*5/9+273.15
            return render_template("temp.html", sum=sum)


@app.route('/length')
def length():
    return render_template("length.html")


@app.route('/length_send', methods=['POST'])
def length_send(sum=sum):
    if request.method == 'POST':
        num = float(request.form['num'])
        convert = request.form['convert']
        if convert == 'From-Kilometers-to-meters':
            sum=num*1000

            return render_template("length.html", sum=sum)
        if convert == 'Meters-to-decimeters':
            sum = num*10

            return render_template("length.html", sum=sum)
        if convert == 'Decimeters-to-centimeters':
            sum = num*10
            return render_template("length.html", sum=sum)

        if convert == 'centimeters-to-millimeters':
            sum = num*10
            return render_template("length.html", sum=sum)


        if convert == 'Meters-to-kilometers':
            sum = num / 1000
            return render_template("length.html", sum = sum)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

if __name__ == '__main__':
    app.run(debug=True)