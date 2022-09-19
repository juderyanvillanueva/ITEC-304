from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <html><body>
            <form action="/greet">
                What's your name? <input type='text' name='username'><br>
                Choose Between RED, GREEN, BLUE? <input type='text' name='color'><br>
                <input type='submit' value='Continue'>
            </form>
        </body></html>
        """

@app.route('/greet')
def greet():
    username = request.args.get('username', 'World')
    color = request.args['color']
    if color == "":
        msg = 'You did not tell any color.'
    if color == "RED":
        msg = color
    elif color == "BLUE":
        msg = color
    elif color == "GREEN":
        msg = color

    return """
        <html><body>
        <form action="/">
            <h2>My Name is {0}, my preferable color is {1}</h2>
            <input type='submit' value='New Input'>
        </form>
        </body></html>
        """.format(username, msg)

# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)
