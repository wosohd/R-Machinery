from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional
from flask_wtf.file import FileField, FileAllowed

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

class MachineForm(FlaskForm):
    name = StringField('Machine Name', validators=[DataRequired()])
    year = StringField('Year of Manufacture', validators=[DataRequired()])
    make_model = StringField('Make/Model', validators=[DataRequired()])
    serial_number = StringField('Serial Number', validators=[Optional()])
    category = SelectField('Category', choices=[
        ('Engines', 'Engines'),
        ('Silage/Forage', 'Silage/Forage'),
        ('Shelling', 'Shelling'),
        ('Milling', 'Milling'),
        ('Irrigation', 'Irrigation'),
        ('Lumbering & Woodwork', 'Lumbering & Woodwork'),
        ('Construction equipments', 'Construction equipments'),
        ('Workshop tools', 'Workshop tools'),
        ('Assorted hard & Power tools', 'Assorted hard & Power tools'),
        ('Generators', 'Generators'),
        ('Tractors', 'Tractors'),
        ('Dairy Farming', 'Dairy Farming'),
        ('Farmyard Structure & Construction', 'Farmyard Structure & Construction'),
        ('Protective Gear', 'Protective Gear'),
        ('Machine Instillation', 'Machine Instillation')
    ], validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class MaintenanceForm(FlaskForm):
    service_date = DateField('Service Date', validators=[DataRequired()])
    technician = StringField('Technician Name', validators=[DataRequired()])
    parts_used = StringField('Parts Used', validators=[Optional()])
    notes = TextAreaField('Service Notes', validators=[Optional()])
    submit = SubmitField('Log Maintenance')

