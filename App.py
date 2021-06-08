from flask import Flask, render_template, request
from werkzeug.utils import redirect
from User.userAccount import *

app = Flask(__name__)

isLogin = False

@app.route('/')
def home():
    return render_template("home.html", data = ["", "Login"])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        details = request.form
        email = details['email']
        password = details['password']
        result = loginCheck(email, password)
        # user = [["dthaa@gmail.com", "dung12345"], ["vuthithuthuy@gmail.com", "thuy12345"]]
        # result = ["admin", "admin"]
        if result[1] == "admin":
            isLogin = True
            return redirect('/admin_user')
        elif result[0] == "True":
            isLogin = True
            return render_template("home.html", data=result)
        else:
            isLogin = False
            return render_template("Login.html", is_login="False")
        
    return render_template("Login.html", is_login="No")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        details = request.form
        email = details['email']
        password = details['password']
        addAccount(email, password)
        return redirect('/login')
        
    return render_template("Register.html", result = False)

@app.route('/admin_user', methods=["GET", "POST"])
def admin_user():
    user = User_list()
    return render_template("admin_user_list.html", user = user)

@app.route('/admin_music', methods=["GET", "POST"])
def admin_music():
    music = Music_list()
    return render_template("admin_music_list.html", music = music)

@app.route('/haha', methods=["GET","POST"])
def haha():
    if request.method == "POST":
        return render_template("sad.html", isBuy="True")
    return render_template("haha.html", isBuy="False")

@app.route('/yay', methods=["GET","POST"])
def yay():
    if request.method == "POST":
        return render_template("yay.html", isBuy="True")
    return render_template("haha.html", isBuy="False")

@app.route('/sad', methods=["GET","POST"])
def sad():
    if request.method == "POST":
        return render_template("sad.html", isBuy="True")
    return render_template("haha.html", isBuy="False")

@app.route('/love', methods=["GET","POST"])
def love():
    if request.method == "POST":
        return render_template("love.html", isBuy="True")
    return render_template("haha.html", isBuy="False")

@app.route('/angry', methods=["GET","POST"])
def angry():
    if request.method == "POST":
        return render_template("angry.html", isBuy="True")
    return render_template("haha.html", isBuy="False")


if __name__ == "__main__":
    app.run(host='0.0.0.0')