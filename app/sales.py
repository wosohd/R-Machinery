from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import app, db
from app.forms import MachineForm
from app.models import Machine

@app.route('/machines/new', methods=['GET', 'POST'])
@login_required
def add_machine():
    form = MachineForm()
    if form.validate_on_submit():
        machine = Machine(
            name=form.name.data,
            year=form.year.data,
            make_model=form.make_model.data,
            serial_number=form.serial_number.data,
            category=form.category.data,
            description=form.description.data,
            owner=current_user
        )
        db.session.add(machine)
        db.session.commit()
        flash('Machine listed successfully!', 'success')
        return redirect(url_for('list_machines'))
    return render_template('add_machine.html', form=form)

@app.route('/machines')
def list_machines():
    machines = Machine.query.all()
    return render_template('machines.html', machines=machines)
