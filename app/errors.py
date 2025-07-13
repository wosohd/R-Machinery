from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors.html', error_code=404), 404

@errors.app_errorhandler(500)
def internal_error(error):
    return render_template('errors.html', error_code=500), 500
