from flask_wtf import Form
from wtforms import TextField, IntegerField
from wtforms.validators import DataRequired

class queryform(Form):
	name = TextField('Item name', validators=[DataRequired()])

class itemform(Form):
	id = IntegerField('ID')
	name = TextField('Name', validators=[DataRequired()])
	description = TextField('Description', validators=[DataRequired()])