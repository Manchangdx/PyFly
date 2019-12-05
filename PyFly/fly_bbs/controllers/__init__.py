from .user_view import user_view

bp_list = [user_view]

def config_blueprints(app):
    for bp in bp_list:
        app.register_blueprint(bp)
