import hashlib
import jwt
import sqlite3
import requests
from flask import Flask, request, jsonify, render_template, redirect, url_for, session, make_response
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = "super_secret_key"

# JWT Secret Key (for demonstration purposes)
JWT_SECRET = "password123"

dFlag = "CCC{default_flag}"
try:
    with open('/flag.txt', 'r') as file:
        dFlag = file.read().strip()
    print(f"Flag is: {dFlag}")

except FileNotFoundError:
    print("The file /app/flag.txt does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

# Helper function for error responses
def error_response(message, status_code=500):
    response = jsonify({'error': message})
    response.status_code = status_code
    return response

# Global error handler for unhandled exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    return error_response(str(e), 500)

# Custom error handler for 404 (Page Not Found)
@app.errorhandler(404)
def page_not_found(e):
    return error_response("Page not found", 404)

# Custom error handler for 403 (Unauthorized)
@app.errorhandler(403)
def unauthorized(e):
    return error_response("Unauthorized access", 403)

# Initialize the database
def init_db():
    try:
        conn = sqlite3.connect('ctf.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT, profile_url TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS secrets (id INTEGER PRIMARY KEY, flag TEXT)''')

        # Insert test users
        c.execute('''INSERT INTO users (username, password, role, profile_url) VALUES ('user', 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', 'user', 'https://www.youtube.com/@CyberHacktivatorsClub')''')
        c.execute('''INSERT INTO users (username, password, role, profile_url) VALUES ('zervaxpwdory','2f7aa82bd3868a52c8db2614e405499b008289838f9f46885908da5422a6b967', 'admin', 'http://127.0.0.1/whtelseyouknow')''')
        #of43iifpowfkwofieqwpofkewfpok admin pass
        conn.commit()
    except sqlite3.Error as e:
        return error_response(f"Database initialization failed: {e}")
    finally:
        conn.close()


@app.route('/logout', methods=['GET'])
def logout():
    # Clear the token cookie
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('token', '', expires=0)
    return resp

# Example route to simulate flag retrieval
@app.route('/whtelseyouknow', methods=['GET'])
def whtelseyouknow():
    try:
        forwarded_for = request.headers.get('X-Forwarded-For', None)

        if forwarded_for != '127.0.0.1':
            return error_response("Unauthorized access", 403)

        return dFlag
    except Exception as e:
        return error_response(f"An error occurred: {e}")

# Homepage route (Login)
@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return error_response(f"Failed to load homepage: {e}")

# Enhanced SQL Injection Filtering function
def is_sql_injection(input_text):
    injection_keywords = ['--', '@@', 'char', 'nchar', 'varchar', 'alter', 'union', 'select', 'insert', 'update', 'delete', 'drop']
    return any(keyword in input_text.lower() for keyword in injection_keywords)

# Helper function to hash passwords using SHA256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role', 'user')  # Default role is 'user'

        try:
            hashed_password = hash_password(password)  # Hash the password

            conn = sqlite3.connect('ctf.db')
            c = conn.cursor()

            # Check if the username already exists
            c.execute("SELECT * FROM users WHERE username = ?", (username,))
            if c.fetchone():
                return error_response("Username already exists", 400)

            # Insert the new user into the database
            c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, hashed_password, role))
            conn.commit()
            return redirect(url_for('index'))
        except sqlite3.Error as e:
            return error_response(f"Registration failed: {e}")
        finally:
            conn.close()

    return render_template('register.html')


# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    try:
        # Check for SQL injection attempts
        if is_sql_injection(username) or is_sql_injection(password):
            return error_response("Invalid credentials :-( SQLI DETECTED", 403)
        hashed_password = hash_password(password)  # Hash the password for comparison
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{hashed_password}'"
        try:
            conn = sqlite3.connect('ctf.db')
            c = conn.cursor()
            c.execute(query)
            user = c.fetchone()
        except sqlite3.Error as e:
            return error_response(f"Database query failed: {e}")
        finally:
            conn.close()

        if user:
            # Generate JWT token
            token = jwt.encode({
                'username': user[1],
                'role': user[3],
                'exp': datetime.utcnow() + timedelta(hours=1)
            }, JWT_SECRET, algorithm='HS256')

            # Save token in cookies
            resp = make_response(redirect(url_for('dashboard')))
            resp.set_cookie('token', token, httponly=True)
            return resp
        else:
            return error_response("Invalid credentials", 401)

    except Exception as e:
        return error_response(f"An error occurred during login: {e}")

# Dashboard route
@app.route('/dashboard', methods=['GET'])
def dashboard():
    token = request.cookies.get('token')
    if not token:
        return redirect(url_for('index'))

    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        username = decoded_token['username']
    except jwt.ExpiredSignatureError:
        return error_response("Token expired", 401)
    except jwt.InvalidTokenError:
        return error_response("Invalid token", 401)

    return render_template('dashboard.html', username=username,role=decoded_token['role'])


# Profile page
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    token = request.cookies.get('token')
    if not token:
        return redirect(url_for('index'))

    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return error_response("Token expired", 401)
    except jwt.InvalidTokenError:
        return error_response("Invalid token", 401)

    role = decoded_token['role']
    username = decoded_token['username']

    if request.method == 'POST':
        new_url = request.form.get('profile_url')
        try:
            conn = sqlite3.connect('ctf.db')
            c = conn.cursor()
            c.execute("UPDATE users SET profile_url=? WHERE role=?", (new_url, role))
            conn.commit()
        except sqlite3.Error as e:
            return error_response(f"Failed to update profile: {e}")
        finally:
            conn.close()

        return redirect(url_for('profile'))

    try:
        conn = sqlite3.connect('ctf.db')
        c = conn.cursor()
        c.execute("SELECT profile_url FROM users WHERE role=?", (role,))
        profile_url = c.fetchone()[0]
    except sqlite3.Error as e:
        return error_response(f"Failed to fetch profile data: {e}")
    finally:
        conn.close()

    return render_template('profile.html', username=username, profile_url=profile_url)

# SSRF vulnerability
@app.route('/fetch_profile_picture', methods=['POST'])
def fetch_profile_picture():
    profile_url = request.form.get('profile_url')

    try:
        response = requests.get(profile_url)
        return f"Fetched content from {profile_url}: {response.text}"
    except requests.RequestException as e:
        return error_response(f"Failed to fetch from {profile_url}: {e}", 500)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0',port='8080')

