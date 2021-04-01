import os

from flask import Flask

#Application Factory - this is used to configure the flask app and return an instance of it
def create_app(test_config=None):
    # create and configure the app. __name__ is a reference to the current python module. 
    # Instance_relative_config means that files are located relatively to the instance folder which is the directory outside flaskr
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        # overrides the default configurations from those in config.py which is found in the instance directory.
        app.config.from_pyfile('config.py', silent=True)

    else:
        # load the test config if passed in
        # test_config is passed in to create_app. Overrides default config as well. This helps use different configurations for tests without having to modify code.
        app.config.from_mapping(test_config)
    
    try:
        # ensures that the instance_path exists. Flask doesnt create the instance folder automatically, but it needs to be made so that the project can can create the SQLite database file there.
        os.makedirs(app.instance_path)
    
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'


    from . import db
    db.init_app(app)

    # import and register the auth blueprint
    from . import auth
    app.register_blueprint(auth.bp)

    # import and register the blog blueprint.
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint = 'index')

    return app
