from flask import Flask


def create_app():
    """Flask application factory."""
    app = Flask(__name__)

    # Register blueprints
    from app.routes import diary
    app.register_blueprint(diary.bp)

    return app
