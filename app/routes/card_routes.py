from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.card import Card
from app.helper_functions import *

card_bp = Blueprint('Cards', __name__, url_prefix='/cards')



#deleting one card
@card_bp.route("/<card_id>", methods=["DELETE"])
def get_one_board(card_id):
    card = get_record_by_id(Card, card_id)
    db.session.delete(card)
    db.session.commit()
    
    return success_message_info_as_list(dict(details=f'Card {card.card_id} "{card.message}" successfully deleted'))


# creating one card
@card_bp.route("", methods=["POST"])
def create_card():
    request_body = request.get_json()
    if "message" not in request_body:
        error_message("Message not found", 400)
    card = Card.self_to_dict(request_body)
    db.session.add(card)
    db.session.commit()
    
    return success_message_info_as_list("Card created successfully", status_code=200)