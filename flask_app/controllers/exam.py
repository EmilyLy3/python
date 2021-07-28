from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models.user import User
from flask_app.models.painting import Painting


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("Please log in to view this page")
        return redirect('/')

    data = {
        'id': session['user_id']
    }

    paintings = Painting.get_all_paintings_with_user()
    purchases = Painting.get_paintings_purchases_by_user_id(data)
    return render_template('dashboard.html', paintings = paintings, purchases = purchases)


@app.route('/add_painting')
def add_painting():
    if 'user_id' not in session:
        flash("Please log in to view this page")
        return redirect('/')

    return render_template('add_painting.html')


@app.route('/insert_painting', methods=['POST'])
def insert_painting():
    # validate form first
    if not Painting.validate_painting(request.form):
        return redirect('/add_painting')

    data = {
        'title': request.form['title'],
        'description': request.form['description'],
        'price': request.form['price'],
        'quantity': request.form['quantity'],
        'count': 0,
        'user_id': session['user_id']
    }

    # insert data into paintings db
    Painting.insert_painting(data)
    return redirect('/dashboard')


@app.route('/edit_painting/<int:painting_id>')
def edit_painting(painting_id):
    if 'user_id' not in session:
        flash("Please log in to view this page")
        return redirect('/')

    data = {
        'id': painting_id
    }

    painting = Painting.get_painting_by_id(data)
    return render_template('edit_painting.html', painting = painting)


@app.route('/update_painting/<int:painting_id>', methods=['POST'])
def update_painting(painting_id):
    # validate first
    if not Painting.validate_painting(request.form):
        return redirect(f'/edit_painting/{painting_id}')

    data = {
        'id': painting_id,
        'title': request.form['title'],
        'description': request.form['description'],
        'price': request.form['price'],
        'quantity': request.form['quantity']
    }

    Painting.update_painting(data)
    return redirect('/dashboard')


@app.route('/delete_painting/<int:painting_id>')
def delete_painting(painting_id):
    data = {
        'id': painting_id
    }

    Painting.delete_painting(data)
    return redirect('/dashboard')


@app.route('/paintings/<int:painting_id>')
def show_painting(painting_id):
    if 'user_id' not in session:
        flash("Please log in to view this page")
        return redirect('/')

    data = {
        'id': painting_id
    }

    painting = Painting.get_all_paintings_with_user_by_painting_id(data)
    return render_template('show_painting.html', painting = painting)


@app.route('/buy_painting/<int:painting_id>', methods=['POST'])
def buy_painting(painting_id):
    data = {
        'id': painting_id,
        'user_id': session['user_id']
    }

    Painting.buy_painting(data)
    return redirect(f'/paintings/{painting_id}')