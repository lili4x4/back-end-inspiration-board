from flask import Blueprint, request, jsonify, make_response
from app import db
from app.helper_functions import create_record_safely, success_message_info_as_list
from app.models.board import Board

board_bp = Blueprint('Boards', __name__, url_prefix='/boards')

@board_bp.route("", methods=["POST"])
def create_new_board():
    request_body = request.get_json()
    new_board = create_record_safely(Board, request_body)

    db.session.add(new_board)
    db.session.commit()

    return success_message_info_as_list(dict(board=new_board.self_to_dict()), 201)
