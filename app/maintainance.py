from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from app import app, db
from app.forms import MaintenanceForm
from app.models import Machine, ServiceLog

@app.route('/machines/<int:machine_id>/maintenance', methods=['GET', 'POST'])
@login_required
def log_maintenance(machine_id):
    form = MaintenanceForm()
    machine = Machine.query.get_or_404(machine_id)
    if form.validate_on_submit():
        log = ServiceLog(
            machine=machine,
            service_date=form.service_date.data,
            technician=form.technician.data,
            parts_used=form.parts_used.data,
            notes=form.notes.data
        )
        db.session.add(log)
        db.session.commit()
        flash('Maintenance logged!', 'success')
        return redirect(url_for('list_machines'))
    return render_template('maintenance.html', form=form, machine=machine)
