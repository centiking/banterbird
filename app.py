from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

def get_db_connection():
    conn = sqlite3.connect('database\database.db')
    conn.row_factory = sqlite3.Row
    return conn


    
@app.route('/')
def index():
    
    print(session)
    if 'username' in session:
        username = session['username']
        return render_template('Home.html', username=username)
    return render_template("Home.html")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/signup')
def signUp():
    return render_template("Signup.html")

@app.route('/login')
def login():
    return render_template("Login.html")

@app.route('/confirm-login', methods=['POST', 'GET'])
def confirm_login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['psw']

        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username=? AND password=?"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            message = "Login successful!"
            print(message)
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = "Invalid credentials. Please try again."
            print(error)
            return render_template("Login.html", error=error)
    
    return render_template("Login.html", error=error)

@app.route('/confirm-signup', methods=['POST'])
def confirm_signup():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['psw']

        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO users (username, password) VALUES (?, ?)"

        try:
            cursor.execute(query, (username, password))
            conn.commit()
            message = "User registered successfully!"
            print(message)
            return redirect(url_for('confirm_login', error=error))
        except Exception as e:
            conn.rollback()
            error = f"Database error: {e}"
            print(error)
        finally:
            conn.close()

        return render_template("Signup.html", error=error)



if __name__ == '__main__':
    app.run(debug=True)
