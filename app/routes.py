from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Rental

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/rentals')
def rentals():
    rentals = Rental.query.all()
    return render_template('rentals.html', rentals=rentals)

@app.route('/add', methods=['GET', 'POST'])
def add_rental():
    if request.method == 'POST':
        rental = Rental(
            title=request.form['title'],
            description=request.form['description'],
            rent_price=request.form['price'],
            billing_date=request.form['billing_date']
        )
        db.session.add(rental)
        db.session.commit()
        return redirect(url_for('rentals'))
    return render_template('add_rental.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_rental(id):
    rental = Rental.query.get_or_404(id)
    if request.method == 'POST':
        rental.title = request.form['title']
        rental.description = request.form['description']
        rental.rent_price = request.form['price']
        rental.billing_date = request.form['billing_date']
        rental.status = request.form['status']
        db.session.commit()
        return redirect(url_for('rentals'))
    return render_template('edit_rental.html', rental=rental)

@app.route('/delete/<int:id>')
def delete_rental(id):
    rental = Rental.query.get_or_404(id)
    db.session.delete(rental)
    db.session.commit()
    return redirect(url_for('rentals'))

@app.route('/login')
def login():
    return render_template('login.html')
