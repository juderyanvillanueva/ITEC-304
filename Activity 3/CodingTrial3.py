from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <html><body>
            <form action="/login">
                <label for='name'>Enter Name</label>
                <input type='text' placeholder='Enter Name' name='name'><br>
                <input type='radio' name='gender' value='Male'>
                <label for='Male'>Male</label>
                <input type='radio' name='gender' value='Female'>
                <label for='Female'>Female</label><br>
                <input type='submit' value='Submit'>
            </form>
        </body></html>
        """

@app.route('/login')
def login():
    name = request.args.get('name', 'World')
    gender = request.args['gender']


    return """
        <html><body>
        <form action="/">
            <h2>{0} is {1} </h2>
        </form>
        </body></html>
        """.format(name, gender)

# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)
