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


app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://inspiration_board_sql_user:vZJG9I6gLoVEiWXotuc9FJAmlHizfU5o@dpg-ch4rjt2ut4m6jh95tdf0-a.ohio-postgres.render.com/inspiration_board_sql"

db.init_app(app)
migrate.init_app(app, db)

# Register Blueprints here
from .routes.board_routes import board_bp
app.register_blueprint(board_bp)
from .routes.card_routes import card_bp
app.register_blueprint(card_bp)

CORS(app)
