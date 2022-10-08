import email
import imp
from pickle import TRUE
from typing import Text
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    text = request.args.get('text')
    password = request.args.get('password')
    email = request.args.get('email')
    gender = request.args['gender']
    birthday = request.args.get('birthday')
    phone = request.args.get('phone')


    return """
        <html>
        <script type="text/javascript" src="{{ url_for('static', filename='script.js')}}"></script>
        <body>
        <form action="/">
            <h2>Username: {0} <br> Password: {1} <br> E-mail: {2} <br> Gender {3} <br> Birthdate: {4} <br> Phone Number: {5}</h2>
        </form>
        </body></html>
        """.format(text, password, email, gender, birthday, phone)
if __name__ == '__main__':
    app.run(debug=TRUE)
