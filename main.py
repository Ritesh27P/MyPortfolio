from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():

    return render_template('contact.html')


@app.route('/project')
def project():
    return render_template('projects.html')

@app.route('/')
def redirect_home():
    return redirect(url_for('home'))


@app.route('/contact-submit', methods=['POST', 'GET'])
def contact_submit():
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
