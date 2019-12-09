from flask import Flask


def create_app():
    #db, blueprints, admin
    # https://github.com/briancappello/flask-react-spa/blob/master/backend/app.py
    app = Flask(__name__)
    configure_app(app)

    return app

def configure_app(app):
    # config, session,..
    ...


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True)