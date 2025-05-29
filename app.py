from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy credentials
USERNAME = "admin"
PASSWORD = "1234"

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == USERNAME and password == PASSWORD:
        return render_template('success.html', user=username)
    else:
        return render_template('failure.html')

if __name__ == '__main__':
    app.run(debug=True)
