from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/navbar')
def navbar():
    options = ['Options', 'Clientes', 'Vendas', 'Recebimentos']
    return render_template('navbar.html', options=options)

if __name__ == '__main__':
    app.run()
