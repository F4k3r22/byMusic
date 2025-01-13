from dataclasses import dataclass
from flask import Flask, render_template, session, redirect, request, flash
import MySQLdb
from TubeKit import YouTubeClient
import random
import string
import time


app = Flask(__name__)

@dataclass
class MySQLConfig:
    """ MySQL Configuration """
    host: str = "localhost"
    user: str = "root"
    password: str = "root"
    database: str = "music"

config = MySQLConfig()
client = YouTubeClient('YOUR_API_KEY')

def testconnetion():
    try:
        print(f"Probando conexión a MySQL con {config}")
        connection = MySQLdb.connect(
            host=config.host,
            user=config.user,
            passwd=config.password,
            db=config.database
        )
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        print(f"Conexión exitosa" if result else "Error en la consulta")

        return "Conexión exitosa" if result else "Error en la consulta"

    except Exception as e:
        return f"Error de conexión: {str(e)}"

# Aun estoy creando las rutas, ya voy a hacer los templates
@app.route('/login')
def login():
    if 'user_id' in session:
        return redirect('/')
    else:
        return render_template('login.html')

@app.route('/register')
def register():
    if 'user_id' in session:
        return redirect('/')
    else:
        return render_template('signup.html')
    
app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/login')

@app.route('login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')
    connection = MySQLdb.connect(
        host=config.host,
        user=config.user,
        passwd=config.password,
        db=config.database
    )

    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM 'users' WHERE 'email' = %s AND 'password' = %s""", (email, password))
    user = cursor.fetchone()
    if user: 
        session['user_id'] = user[0]
        cursor.close()
        return redirect('/')
    else: 
        flash('Sorry, wrong email or password, Please try again or reset your password', 'danger')
        cursor.close()
        return redirect('/login')

@app.route('add_user', methods=['POST'])
def add_user():
    name = request.form.get('name')
    email = request.form.get('email')
    pno = request.form.get('fullPhoneNumber')
    password = request.form.get('password')
    gender = request.form.get('gender')
    user_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    connection = MySQLdb.connect(
        host=config.host,
        user=config.user,
        passwd=config.password,
        db=config.database
    )
    cursor = connection.cursor()
    try:
        cursor.execute(f""" INSERT INTO 'users' ('name', 'email', 'pno', 'password', 'user_id', 'gender') VALUES(%s, %s, %s, %s, %s, %s)""", (name, email, pno, password, user_id, gender))
        connection.commit()
        flash('Account created successfully', 'success')
        time.sleep(3)
    except Exception as e:
        connection.rollback()
        flash('Something went wrong, Please try again', 'error')
        return redirect('/register')
    finally:
        cursor.close()
        connection.close()
        return redirect('/login')

@app.route('/')
def index():
    pass

