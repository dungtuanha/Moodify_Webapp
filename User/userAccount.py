from User.DB import *

def loginCheck(email, password):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    user = cursor.fetchall()
    if email == "admin@admin" and password == "admin":
        return ["True","admin"]
    
    for i in range(0, len(user)):
        if email == user[i][0] and password == user[i][1]:
            email = email.split("@")
            username = email[0]
            result = ["True", username]
            return result
    
    return ["False", ""]

def addAccount(email, password):
    qr = "INSERT INTO user (email, password) VALUES ('"+ email +"','"+ password + "')"
    cursor.execute(qr)
    conn.commit()

def User_list():
    cursor.execute("SELECT * FROM user")
    user = cursor.fetchall()
    return user

def Music_list():
    cursor.execute("SELECT * FROM music")
    music = cursor.fetchall()
    return music
