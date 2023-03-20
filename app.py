from flask import Flask, render_template, request
import sqlite3 as sql
from passlib.hash import sha256_crypt


app = Flask(__name__)

host = 'http://127.0.0.1:5000/'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/name', methods=['POST', 'GET'])
def name():
    error = None
    if request.method == 'POST':
        result = valid_name(request.form['FirstName'], request.form['LastName'])
        if result:
            return render_template('home.html', error=error, result=result)
        else:
            error = 'invalid login'
    return render_template('input.html', error=error)


def valid_name(first_name, last_name):
    connection = sql.connect('database.db')
    cursor = connection.execute(f'SELECT * FROM users WHERE firstname=? AND lastname=?;',(first_name, last_name))
    connection.commit()
    #cursor = connection.execute('SELECT * FROM users;')
    return cursor.fetchall()


if __name__ == "__main__":
    app.run()


