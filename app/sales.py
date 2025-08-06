from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from . import db
from app.forms import MachineForm
from app.models import Machine

sales = Blueprint('sales', __name__)

@sales.route('/machines')
def list_machines():
    page = request.args.get('page', 1, type=int)
    category = request.args.get('category')
    search = request.args.get('search')

    query = Machine.query

    if category:
        query = query.filter(Machine.category.ilike(f"%{category}%"))
    if search:
        query = query.filter(Machine.name.ilike(f"%{search}%"))

    machines = query.order_by(Machine.year.desc()).paginate(page=page, per_page=6)
    return render_template('machines.html', machines=machines)

@sales.route('/machine/<int:machine_id>')
def machine_detail(machine_id):
    machine = Machine.query.get_or_404(machine_id)
    return render_template('machine_detail.html', machine=machine)

@sales.route('/add_machine', methods=['GET', 'POST'])
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
            is_sold=False,
            user_id=current_user.id
        )
        db.session.add(machine)
        db.session.commit()
        flash('Machine listing added successfully!', 'success')
        return redirect(url_for('sales.list_machines'))
    return render_template('add_machine.html', form=form)

