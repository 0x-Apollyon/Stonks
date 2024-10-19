import flask
from markupsafe import escape
from markupsafe import Markup
from flask import Flask, render_template , request
#import argon2

app = Flask(__name__)

@app.route("/" ,methods = ['GET'])
def main_page():
    return render_template('main.html')

@app.route("/login" ,methods = ['GET'])
def login_page():
    return render_template('login.html')

@app.route("/signup" ,methods = ['GET'])
def signup_page():
    return render_template('signup.html')

@app.route("/create_account" ,methods = ['POST'])
def account_creation():
    account_data = request.get_json() 
    print(account_data)
    password = account_data["password"]
    confirm_password = account_data["confirmPassword"]
    username = account_data["username"]
    name = account_data["name"]
    email = account_data["email"]
    #account_data --> {'name': '', 'username': '', 'email': '', 'password': '', 'confirmPassword': ''}
    if password != confirm_password:
       return {"error":"Password and confirmed password do not match"} , 201
    
    if len(password) > 256:
        return {"error":"Password can not be longer than 256 characters"} , 201

    return 200    

    
    print(account_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1000) 
