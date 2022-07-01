import pytest
from app.models.board import Board
from app.models.card import Card

#Board tests:

def test_get_one_saved_board_no_cards(client, one_board_no_cards):
    #Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert "board" in response_body

def test_get_board_not_found(client):
    #Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 404
    assert response_body == {"details": "Board id: 1 not found"}

def test_get_boards_no_boards(client):
    #Act
    response = client.get("/boards")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_board_with_cards(client, one_board_no_cards):
    #Arrange
    card_1 = {
            "message": "The woods are lovely, dark and deep..."
        }
    card_2 = {
            "message": "Las ramas de los árboles están envueltas en fundas de hielo."
        }

    #Act
    client.post("/boards/1/cards", json=card_1)
    client.post("/boards/1/cards", json=card_2)

    response = client.get("/boards/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body["board"]["title"] == "Winter"
    assert response_body["board"]["owner"] == "Lili"
    assert response_body["board"]["cards"] == [
        {
            "board_id": 1,
            "card_id": 1,
            "likes_count": 0,
            "message": "The woods are lovely, dark and deep..."
        },
        {
            "board_id": 1,
            "card_id": 2,
            "likes_count": 0,
            "message": "Las ramas de los árboles están envueltas en fundas de hielo."
        }
    ]

def test_get_two_boards_no_cards(client, two_boards_no_cards):
    response = client.get("/boards")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0]["title"] == "Winter"
    assert response_body[0]["owner"] == "Lili"
    assert response_body[0]["cards"] == []
    assert response_body[1]["title"] == "Spring"
    assert response_body[1]["owner"] == "Adriana"
    assert response_body[1]["cards"] == []

def test_get_cards_for_board_with_no_cards(client, one_board_no_cards):
    response = client.get("/boards/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body["board"]["cards"] == []

#Card tests
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

def test_create_card_invalid_data(client, one_board_no_cards):
    #Act
    response = client.post("/boards/1/cards", json={
        "messag": "Peppermint mocha, yum"
    })
    response_body = response.get_json()

    #Assert
    assert response.status_code == 400
    assert response_body == {"details": "Message not found"}