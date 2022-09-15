from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <html><body>
            <form action="/greet">
                What's your name? <input type='text' name='username'><br>
                What's your personality? <input type='text' name='personality'><br>
                <input type='submit' value='Continue'>
            </form>
        </body></html>
        """

@app.route('/greet')
def greet():
    username = request.args.get('username', 'World')
    personality = request.args['personality']
    if personality == "":
        msg = 'You did not tell me your personality.'
    else:
        msg = personality

    return """
        <html><body>
        <form action="/">
            <h2>{0} is {1}</h2>
            <input type='submit' value='New Input'>
        </form>
        </body></html>
        """.format(username, msg)

# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)
