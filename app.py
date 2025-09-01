from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return '<h2>Welcome! Go to <a href="/login">Login Page</a></h2>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == '1234':
            return f"<h3>Welcome back, {username}!</h3>"
        else:
            return "<h3>Invalid credentials. Try again.</h3>"
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
