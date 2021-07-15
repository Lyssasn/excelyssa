import os
import time
from flask import Flask
from . import db, auth


def log_time(f):
    def decorator(*args, **kw):
        print(f'{time.time()}')
        return f(*args, **kw)
    return decorator


@log_time
def create_app(test_config=None):
    # create and configure app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='qmTdtaGZWbX1lWtxuEp8aswAZuS4QQq7',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
    )

    if test_config is None:
        # load config instance if exist
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load test config
        app.config.from_mapping(test_config)

    # ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # init db
    with app.app_context():
        db.init_app(app)

    # registering auth app
    app.register_blueprint(auth.bp)

    # register company app
    from . import company
    app.register_blueprint(company.bp)
    app.add_url_rule('/', endpoint='index')
  
    return app
