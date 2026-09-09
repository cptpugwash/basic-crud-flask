from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class queryform(FlaskForm):
	name = StringField('Item name', validators=[DataRequired()])

class itemform(FlaskForm):
	id = IntegerField('ID')
	name = StringField('Name', validators=[DataRequired()])
	description = StringField('Description', validators=[DataRequired()])