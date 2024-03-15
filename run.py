from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<center><h1></h1></center>'

@app.route('/suma/<int:num1>/<int:num2>') #suma de dos numeros
@app.route('/suma/<int:num1>/<int:num2>/<int:num3>') #suma de tres numeros
@app.route('/suma/<int:num1>/<int:num2>/<int:num3>/<int:num4>') #suma de cuatro numeros
def suma(num1, num2, num3 = None, num4 = None):
    if num4 == None and num3 == None:
        resul = num1 + num2
        return f'<center><h1>{num1} + {num2} = {resul}</h1></center>'
    elif num4 == None:
        resul = num1 + num2 + num3
        return f'<center><h1>{num1} + {num2} + {num3} = {resul}</h1></center>'
    else:
        resul = num1 + num2 + num3 + num4
        return f'<center><h1>{num1} + {num2} + {num3} + {num4} = {resul}</h1></center>'

if __name__ == '__main__':
    app.run(port=5500, debug=True )