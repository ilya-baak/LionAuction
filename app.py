from flask import Flask, render_template, request
import sqlite3 as sql
from passlib.hash import sha256_crypt


app = Flask(__name__)

host = 'http://127.0.0.1:5000/'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        result = valid_login(request.form['UserName'], request.form['Password'])
        if result:
            return render_template('home.html', error=error, result=result)
        else:
            error = 'Invalid login credentials. Please try again.'
    return render_template('login.html', error=error)


def valid_login(user_name, password_in):
    connection = sql.connect('database.db')
    cursor = connection.execute(f'SELECT * FROM users WHERE username=? AND password=?;',(user_name, password_in))
    connection.commit()
    return cursor.fetchall()

def hash_passwords(password):
    hash = sha256_crypt.hash(password)



if __name__ == "__main__":
    app.run()


