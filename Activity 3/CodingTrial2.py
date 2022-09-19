from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <html><body>
            <form action="/login">
                <label for='username'>Enter Username</label>
                <input type='text' placeholder='Enter Username' name='username'><br>
                <label for="password">Enter Password</label>
                <input type='password' placeholder='Enter Password' name='password'><br>
                <input type='submit' value='Login'>
            </form>
        </body></html>
        """

@app.route('/login')
def login():
    username = request.args.get('username', 'World')
    password = request.args['password']
    if password == "":
        msg = 'Please input your password'

    return """
        <html><body>
        <form action="/">
            <h2>{0}'s account logged in successfully </h2>
        </form>
        </body></html>
        """.format(username)

# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)
