from app import db, login_manager
from flask_login import UserMixin
from datetime import date

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)
    machines = db.relationship('Machine', backref='owner', lazy=True)

class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    make_model = db.Column(db.String(70), nullable=False)
    serial_number = db.Column(db.String(50), unique=True)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.Date, default=date.today)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    service_logs = db.relationship('ServiceLog', backref='machine', lazy=True)

class ServiceLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.Integer, db.ForeignKey('machine.id'), nullable=False)
    service_date = db.Column(db.Date, nullable=False)
    technician = db.Column(db.String(100), nullable=False)
    parts_used = db.Column(db.Text)
    notes = db.Column(db.Text)
