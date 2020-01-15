from flask import Flask
from flask_restful import Api

from db import db, migrate
from src.config import run_config
from src.resources.errorhandling import page_not_found
from src.resources.healthcheck import HealthcheckView
from src.resources.user import UserView


def create_app():
    app = Flask(__name__)
    api = Api(app)
    configure_app(app)

    app.register_error_handler(404, page_not_found)

    api.add_resource(HealthcheckView, '/healthcheck', '/')
    api.add_resource(UserView, '/users', '/users/<int:id>')



    return app


def configure_app(app):
    # config, session,..
    app.config.from_object(run_config())

    db.init_app(app)
    db.drop_all(app=app)
    db.create_all(app=app)
    migrate.init_app(app, db)

    # @app.before_first_request
    # def create_tables():
    #     db.drop_all(app=app)
    #     db.create_all(app=app)
    #     # db.session = db_init_room(db)
    #     #
    #     # db.session = db_init_stuff(db)
    #     # db.session = db_init_tenant(db)
    #     # db.session = db_init_stuff_to_room(db)
    #     # db.session.commit()

if __name__ == '__main__':
    app = create_app()

    app.run(host='0.0.0.0', debug=True)
