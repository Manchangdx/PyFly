from flask import Flask

from .config import configs
from .controllers import config_route


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    config_route(app)

    return app
