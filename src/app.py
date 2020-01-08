from flask import Flask

from db import db, migrate
from src.config import run_config


def create_app():
    #db, blueprints, admin
    # https://github.com/briancappello/flask-react-spa/blob/master/backend/app.py
    app = Flask(__name__)
    configure_app(app)

    return app

def configure_app(app):
    # config, session,..
    app.config.from_object(run_config())
    db.init_app(app)
    db.create_all(app=app)
    migrate.init_app(app,db)


    @app.route('/')
    @app.route('/index')
    def index():
        return "Index page\n"


if __name__ == '__main__':
    app = create_app()

    app.run(host='0.0.0.0', debug=True)