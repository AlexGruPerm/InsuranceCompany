from app import app
from flask import render_template

@app.route('/agents')
def view_agents():
    #return "Hello, World! 123"
    #return render_template('base.html')
    user = {'nickname': 'Miguel2'}  # выдуманный пользователь
    users= {}
    for i in range(1,15,1):
        #users["k"+str(i)]="First Name_"+str(i)
        users["k" + str(i)] = {"FirstName":"First Name_" + str(i),"Surname":"Surname_"+str(i*100)}
    return render_template("agents_list.html",
                           title='Home',
                           user=user,
                           users=users)
