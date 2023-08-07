from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'  # SQLite database file
db = SQLAlchemy(app)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"<Client {self.name}>"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clients')
def client_management():
    clients = Client.query.all()
    return render_template('clients.html', clients=clients)

@app.route('/add-client', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        new_client = Client(name=name, email=email, phone=phone)
        db.session.add(new_client)
        db.session.commit()

        return redirect(url_for('client_management'))

    return render_template('add_client.html')

@app.route('/edit-client/<int:client_id>', methods=['GET', 'POST'])
def edit_client(client_id):
    client = Client.query.get_or_404(client_id)

    if request.method == 'POST':
        client.name = request.form['name']
        client.email = request.form['email']
        client.phone = request.form['phone']
        db.session.commit()

        return redirect(url_for('client_management'))

    return render_template('edit_client.html', client=client)

@app.route('/delete-client/<int:client_id>')
def delete_client(client_id):
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()

    return redirect(url_for('client_management'))

@app.route('/sales')
def sales():
    return render_template('sales.html')

@app.route('/income')
def income():
    return render_template('income.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()