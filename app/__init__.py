from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from datetime import datetime

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'danger'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '0702085689'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Register Blueprints
    from app.routes import main as main_blueprint
    from app.sales import sales as sales_blueprint
    from app.maintenance import maintenance as maintenance_blueprint
    from app.errors import errors as errors_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(sales_blueprint)
    app.register_blueprint(maintenance_blueprint)
    app.register_blueprint(errors_blueprint)


    @app.context_processor
    def inject_current_year():
        return {'current_year': datetime.now().year}

    return app


