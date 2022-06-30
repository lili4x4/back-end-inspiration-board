import pytest
from app.models.board import Board

def test_get_one_saved_board_no_cards(client, one_board_no_cards):
    #Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert "board" in response_body
    assert response_body == {
        "board": {
        "cards": [],
        "id": 1,
        "owner": "Lili",
        "title": "Winter"
    }
    }
