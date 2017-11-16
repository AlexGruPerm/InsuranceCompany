from app import app
from flask import render_template

@app.route('/agents')
def view_agents():
    #return "Agents page!"
    return render_template('agents_list.html')