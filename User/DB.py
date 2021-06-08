from flask import Flask
from flaskext.mysql import MySQL

mysql = MySQL()

app = Flask(__name__)

app.config["MYSQL_DATABASE_USER"] = 'dthaa'
app.config["MYSQL_DATABASE_PASSWORD"] = 'dung12345'
app.config["MYSQL_DATABASE_DB"] = 'moodify'
app.config["MYSQL_DATABASE_HOST"] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()

def loginCheck(email, password):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    user = cursor.fetchall()
    if email == "admin@admin" and password == "admin":
        return ["True","admin"]