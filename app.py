from flask import Flask, render_template, request, session
import secrets
import sqlite3 as sql
from passlib.hash import sha256_crypt


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
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
        session['username'] = username
        session['role'] = role
        result = valid_login(username, password, role)
        # Need to check what type of role: Bidder, HelpDesk, or Seller
        if result:
            connection = sql.connect('database.db')
            cursor = connection.execute('SELECT * FROM Bidder WHERE email=?;', (username,))
            bidder = cursor.fetchone()
            connection.commit()
            return render_template('home.html', error=error, result=result, user=bidder, role=role)
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
    user = session.get('username')
    role = session.get('role')
    connection = sql.connect('database.db')
    cursor = connection.execute('SELECT * FROM Bidder WHERE email=?;', (user,))
    user = cursor.fetchone()
    return render_template('home.html', user=user, role=role)


@app.route('/account', methods=['POST', 'GET'])
def account():
    user = session.get('username')
    role = session.get('role')
    connection = sql.connect('database.db')
    cursor = connection.execute('SELECT * FROM Seller WHERE email=?;', (user,))
    isSeller = cursor.fetchone()

    if isSeller:
        bankInfo = isSeller
    else:
        bankInfo = None
    isHelpDesk = connection.execute('SELECT * FROM helpdesk WHERE email=?;', (user,)).fetchone()

    if isHelpDesk:
        position = isHelpDesk
    else:
        position = None

    cursor = connection.execute('SELECT * FROM Bidder WHERE email=?;', (user,))
    info = cursor.fetchone()
    address = connection.execute('SELECT * FROM Address WHERE address_id=?;', (info[5],)).fetchone()
    zip = connection.execute('SELECT * FROM Zipcode_Info WHERE zipcode=?;', (address[1],)).fetchone()
    credit = connection.execute('SELECT * FROM Credit_Cards WHERE Owner_email=?;', (user,)).fetchone()
    digits = credit[0][-4:]
    return render_template('account.html', info=info, address=address,
                           zip=zip, bankInfo=bankInfo, digits=digits, role=role, position=position)

@app.route('/categories', methods=['POST', 'GET'])
def categories():
    connection = sql.connect('database.db')
    #Fetch unique parent categories
    categories = connection.execute('SELECT DISTINCT parent_category FROM Categories ORDER BY parent_category').fetchall()
    #Removes unwanted characters from category
    items = [item[0] for item in categories]
    connection.close()
    return render_template('categories.html', items=items)

@app.route('/subcategory', methods=['POST', 'GET'])
def subcategory():
    category = request.form.get('category')
    connection = sql.connect('database.db')
    items = connection.execute('SELECT category_name FROM Categories WHERE parent_category=?;',
                                       (category,)).fetchall()
    subcategories = [item[0] for item in items]
    return render_template('subcategory.html', subcategories=subcategories)



if __name__ == "__main__":
    app.run()


