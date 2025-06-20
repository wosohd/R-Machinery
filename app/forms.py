from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired, NumberRange

CATEGORIES = [
    'Engines', 'Silage/Forage', 'Shelling', 'Milling', 'Irrigation', 'Lumbering & Woodwork',
    'Construction equipments', 'Workshop tools', 'Assorted hard & Power tools', 'Generators', 'Tractors', 
    'Dairy Farming', 'Farmyard Structure & Construction', 'Protective Gear', 'Machine Instillation'
]

class MachineForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired(), NumberRange(min=1950, max=2035)])
    make_model = StringField('Make & Model', validators=[DataRequired()])
    serial_number = StringField('Serial Number', validators=[DataRequired()])
    category = SelectField('Category', choices=[(cat, cat) for cat in CATEGORIES])
    description = TextAreaField('Description')
    submit = SubmitField('Add Machine')

class MaintenanceForm(FlaskForm):
    service_date = DateField('Service Date', format='%Y-%m-%d', validators=[DataRequired()])
    technician = StringField('Technician Name', validators=[DataRequired()])
    parts_used = TextAreaField('Parts Used')
    notes = TextAreaField('Additional Notes')
    submit = SubmitField('Log Maintenance')
