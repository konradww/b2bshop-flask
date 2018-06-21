from flask import Flask
from flask_table import Table, Col, LinkCol
from flask_mysqldb import MySQL
from flask import render_template
import os

app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'MYsql123'
app.config['MYSQL_DB'] = 'TEST'

mysql = MySQL(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/result')
def search_results():
    cur = mysql.connection.cursor()
    cur.execute('''Select * from test''')
    results = cur.fetchall()
    return render_template('result.html', result=results)

if __name__ == '__main__':
    app.run()



