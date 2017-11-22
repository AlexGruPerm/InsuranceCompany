from flask.ext.wtf import FlaskForm
from wtforms import  BooleanField
from wtforms.fields import StringField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    openid = StringField('openid', validators = [DataRequired()])
    remember_me = BooleanField('remember_me', default = False)