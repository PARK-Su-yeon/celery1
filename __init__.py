

def create_app(app):
    app = Flask(__name__)
    celery.conf.update(app)
    return app
