# from flask import Flask, jsonify
# from flask_cors import CORS
# from flask_restx import Api
# from flask_sqlalchemy import SQLAlchemy
#
#
# def create_app(env=None):
#     from app.config import config_by_name
#     from app.routes import register_routes
#
#     app = Flask(__name__)
#     app.config.from_object(config_by_name[env or "test"])
#     api = Api(app, title="UdaConnect Person API", version="0.1.0")
#
#     CORS(app)  # Set CORS for development
#
#     register_routes(api, app)
#     db.init_app(app)
#
#     @app.route("/health")
#     def health():
#         return jsonify("healthy")
#
#     return app

# import sqlalchemy
#
# # DB_USERNAME = os.environ["DB_USERNAME"]
# # DB_PASSWORD = os.environ["DB_PASSWORD"]
# # DB_HOST = os.environ["DB_HOST"]
# # DB_PORT = os.environ["DB_PORT"]
# # DB_NAME = os.environ["DB_NAME"]
#
# DB_USERNAME = 'boram'
# DB_PASSWORD = 'boram'
# DB_HOST = 'localhost'
# DB_PORT = 5432
# DB_NAME = 'geoconnections'
#
# SQLALCHEMY_DATABASE_URI = (
#     f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# )
# db = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI)

