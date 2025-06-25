from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from . import db
from app.forms import MaintenanceForm
from app.models import Machine, ServiceLog

maintenance = Blueprint('maintenance', __name__)

@maintenance.route('/machines/<int:machine_id>/maintenance', methods=['GET', 'POST'])
@login_required
def log_maintenance(machine_id):
    form = MaintenanceForm()
    return render_template('maintenance.html', form=form)

