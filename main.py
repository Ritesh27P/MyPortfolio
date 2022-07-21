from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/')
def redirect_home():
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
