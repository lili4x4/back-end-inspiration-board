import pytest
from app.models.board import Board
from app.models.card import Card

def test_get_one_saved_board_no_cards(client, one_board_no_cards):
    #Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert "board" in response_body


def test_create_card(client, one_board_no_cards):
    #Act
    response = client.post("/boards/1/cards", json={
        "message": "Peppermint mocha, yum"
    })
    response_body = response.get_json()

    #Assert
    assert response.status_code == 201
    assert response_body == "Card created successfully"

    new_card = Card.query.get(1)
    assert new_card
    assert new_card.message == "Peppermint mocha, yum"
    assert new_card.likes_count == 0