from flask_pymongo import PyMongo


mongo = PyMongo()


def init_extensions(app):
    mongo.init_app(app)
