from flask import Flask, request, render_template, redirect
from datetime import datetime
import csv

# Initialize Flask app
app = Flask(__name__)
print('Iniciando o programa...')

@app.route('/', methods=['GET', 'POST'])
def index():
    ip = request.remote_addr
    data_hora = datetime.now()

    if request.method == 'POST':
        nome = request.form.get('nome')
        telefone = request.form.get('telefone')
        email = request.form.get('email')

        # Salvar contato
        with open('contatos.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([ip, data_hora.strftime('%d/%m/%Y'), data_hora.strftime('%H:%M:%S'), nome, telefone, email])

        #return redirect('/')
        return redirect('http://www.example.com')

    # Salvar acesso (sempre que a página for carregada)
    with open('acessos.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([ip, data_hora.strftime('%d/%m/%Y'), data_hora.strftime('%H:%M:%S')])

    return render_template('index.html')

@app.route('/acessos')
def mostrar_acessos():
    acessos = []
    try:
        with open('acessos.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            acessos = list(reader)
    except FileNotFoundError:
        acessos = []

    return render_template('acessos.html', acessos=acessos)

@app.route('/contatos')
def mostrar_contatos():
    contatos = []
    try:
        with open('contatos.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            contatos = list(reader)
    except FileNotFoundError:
        contatos = []

    return render_template('contatos.html', contatos=contatos)


if __name__ == '__main__':
    app.run(debug=True)
