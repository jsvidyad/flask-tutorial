import os
from flask import Flask, url_for, redirect, current_app

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev', 
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        ...
        
    @app.route('/')
    def hello():
        return redirect(url_for('blog.index'))
    
    from . import db, auth, blog
    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', 'index')
    
    return app


# app = create_app()

# with app.test_request_context():
#     print(url_for('auth.register'))
#     print(url_for('auth.login'))
#     print(url_for('auth.logout'))
#     print(url_for('blog.index'))
#     print(url_for('blog.create'))
#     print(url_for('blog.update', id=1))
#     print(url_for('blog.delete', id=1))
