from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    #return "Hello, World! 123"
    return render_template('base.html')