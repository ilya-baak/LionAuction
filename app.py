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
        username = request.form['UserName']
        password = request.form['Password']
        role = request.form['role']
        result = valid_login(username, password, role)
        # Need to check what type of role: Bidder, HelpDesk, or Seller
        if result:
            connection = sql.connect('database.db')
            cursor = connection.execute('SELECT * FROM Bidder WHERE email=?;', (username,))
            bidder = cursor.fetchone()
            connection.commit()
            return render_template('home.html', error=error, result=result, bidder=bidder, role=role)
        else:
            error = 'Invalid login credentials. Please try again.'
    return render_template('login.html', error=error)


def valid_login(user_name, password_in, role):
    connection = sql.connect('database.db')
    validRole = connection.execute('SELECT * FROM ' + role +' WHERE email=?;', (user_name,)).fetchone()
    if not validRole:
        isMatch = None
        return isMatch
    cursor = connection.execute('SELECT * FROM users WHERE username=?;', (user_name,))
    connection.commit()
    try:
        hashedPassword = cursor.fetchone()[1]
        isMatch = sha256_crypt.verify(password_in, hashedPassword)
    except:
        isMatch = None
    return isMatch


@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()


