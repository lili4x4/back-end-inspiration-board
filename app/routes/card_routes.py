from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.card import Card

card_bp = Blueprint('Cards', __name__, url_prefix='/cards')
