from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')

def db_connection():
    connection = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )
    return connection


@app.route('/')
def index():
    conn = db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM user')
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('test.html', user=products)

