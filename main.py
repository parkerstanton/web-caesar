from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form{
                background-color: #eee;
                padding: 20px;
                margin 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
    <form action="/" method="post">
    <label for="rotate">Rotate By</label>
    <input type="text" name="rot" id="rotate" value="0">
    <textarea name="text">
    </textarea>
    <input type="submit" name="Submit Query">
    </form>
    
</html>


"""
@app.route("/", methods=['POST'])
def encrypt():
    rotation_number = int(request.form['rot'])
    encrypt_text = request.form['text']
    return "<h1>" + rotate_string(encrypt_text,rotation_number) + "</h1>"




@app.route("/")
def index():
    return form

app.run()