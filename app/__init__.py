from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
db.init_app(app)
migrate.init_app(app, db)

# Register Blueprints here
from .routes.board_routes import board_bp
app.register_blueprint(board_bp)
from .routes.card_routes import card_bp
app.register_blueprint(card_bp)

CORS(app)
