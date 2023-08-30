import sqlite3
def check_if_user_exists(user_email):
    conn = sqlite3.connect("/data/user.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (user_email,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def authenticate_user(email, password):
    conn = sqlite3.connect("/data/user.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE email = ? AND password = ?"
    cursor.execute(query, (email, password))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def add_user(email,password):
    conn = sqlite3.connect("/data/user.db")
    cursor = conn.cursor()
    query = "INSERT INTO users (email, password) VALUES (?,?)"
    cursor.execute(query,(email,password))
    conn.commit()
    conn.close()

def get_all_user_data():
    conn = sqlite3.connect('/data/user.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    user_data = cursor.fetchall()
    conn.close()
    return user_data

def update_name_quote(name, quote, email):
    db = sqlite3.connect("/data/user.db")
    cursor = db.cursor()
    query = "UPDATE users SET name = ?, quote = ? WHERE email = ?"
    cursor.execute(query, (name, quote, email))
    db.commit()
    db.close()

def get_status(email):
    stat = True
    conn = sqlite3.connect("/data/user.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    if result[6] == 1: # takes a none type value
        stat = False
    return stat

def has_submitted(email):
    conn = sqlite3.connect("/data/user.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET submission = ? WHERE email = ?",(1 , email))
    conn.commit()
    conn.close()
