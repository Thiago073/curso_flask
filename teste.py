from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/')
def raiz():
    return 'GG Rapaziada, P E R D E M O'

@app.route('/page2')
def page2():
    return '<h1>GG top</h1>'

# Passagem de parâmetro na rota é feita com os <>, exemplo: <string:nome>
@app.route('/pessoa/<string:nome>/<string:cidade>')
def pessoa(nome, cidade):
    # Passagem de parâmetro via Json 
    return jsonify({'Nome':nome, 'Cidade':cidade})

@app.route('/soma/<int:num1>/<int:num2>')
def soma(num1,num2):
    somar = num1 + num2
    return f'A soma dos dois números é: {somar}'

app.run(debug=True)