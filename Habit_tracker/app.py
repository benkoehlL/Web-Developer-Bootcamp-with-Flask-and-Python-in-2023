import os
from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.jinja_env.lstrip_blocks = True
    app.jinja_env.trim_blocks = True
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.get_default_database()
    app.register_blueprint(pages)
    
    return app