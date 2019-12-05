from flask import Flask

from .config import configs
from .controllers import config_blueprints
from .install_init import init as install_init
from .extensions import init_extensions


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    init_extensions(app)
    config_blueprints(app)
    install_init()
    return app
