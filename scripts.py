from passlib.hash import sha256_crypt
import sqlite3 as sql

def hash_passwords():
    connection = sql.connect('database.db')
    cursor = connection.cursor()
    cursor2 = connection.cursor()
    # Fetch all passwords
    passwords = cursor.execute('SELECT * FROM users;').fetchall()
    for passw in passwords:
        rowPassword = passw[1]
        hashedPassword = sha256_crypt.hash(rowPassword)
        cursor2.execute('UPDATE users SET hashedpass=? WHERE password=?;', (hashedPassword, rowPassword))
    connection.commit()
    connection.close()
    print("Database populated successfully")

