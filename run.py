from flask import Flask #Hecho por cristofep

app = Flask(__name__)

@app.route('/')
def index():
    return '<center><h1></h1></center>'

# Suma
@app.route('/suma/<int:num1>/<int:num2>') #suma de dos numeros
@app.route('/suma/<int:num1>/<int:num2>/<int:num3>') #suma de tres numeros
@app.route('/suma/<int:num1>/<int:num2>/<int:num3>/<int:num4>') #suma de cuatro numeros
def suma(num1, num2, num3 = None, num4 = None):
    if num4 == None and num3 == None:
        resul = num1 + num2 #Hecho por cristofep
        return f'<center><h1>{num1} + {num2} = {resul}</h1></center>'
    elif num4 == None:
        resul = num1 + num2 + num3
        return f'<center><h1>{num1} + {num2} + {num3} = {resul}</h1></center>'
    else:
        resul = num1 + num2 + num3 + num4
        return f'<center><h1>{num1} + {num2} + {num3} + {num4} = {resul}</h1></center>'

# Resta
@app.route('/resta/<int:num1>/<int:num2>') #Resta de dos numeros
@app.route('/resta/<int:num1>/<int:num2>/<int:num3>') #Resta de tres numeros
@app.route('/resta/<int:num1>/<int:num2>/<int:num3>/<int:num4>') #Resta de cuatro numeros
def resta(num1, num2, num3 = None, num4 = None):
    if num4 == None and num3 == None:
        resul = num1 - num2
        return f'<center><h1>{num1} - {num2} = {resul}</h1></center>'
    elif num4 == None:
        resul = num1 - num2 - num3
        return f'<center><h1>{num1} - {num2} - {num3} = {resul}</h1></center>'
    else: #Hecho por cristofep
        resul = num1 - num2 - num3 - num4
        return f'<center><h1>{num1} - {num2} - {num3} - {num4} = {resul}</h1></center>'

# Multiplicancion
@app.route('/multiplicacion/<num1>/<num2>')
def multiplicacion(num1, num2):
    resul = num1 * num2
    return f'<center><h1>{num1} x {num2} = {resul}</h1></center>'

# Divicion
@app.route('/divicion/<num1>/<num2>')
def divicion(num1, num2):#Hecho por cristofep
    resul = num1 / num2
    return f'<center><h1>{num1} ÷ {num2} = {resul}</h1></center>'

# Divicion
@app.route('/potencia/base>/<num1>')
@app.route('/potencia/<base>/<num1>/<num2>')
@app.route('/potencia/<base>/<num1>/<num2>/<num3>')
def potencia(base, num1, num2 ,num3):#Hecho por cristofep
    if num3 == None and num2 == None:
        resul = base ** num1
        return f'<center><h1>{base} ^ {num1} = {resul}</h1></center>'
    elif num3 == None:
        resul = base ** num1 ** num2
        return f'<center><h1>{base} ^ {num1} ^ {num2} = {resul}</h1></center>'
    else: #Hecho por cristofep
        resul = base ** num1 ** num2 ** num3
        return f'<center><h1>{base} ^ {num1} ^ {num2} ^ {num3} = {resul}</h1></center>'

if __name__ == '__main__':
    app.run(port=5500, debug=True )#Hecho por cristofep