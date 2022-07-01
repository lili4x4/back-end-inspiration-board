import pytest
from app import create_app
from app import db
from app.models.board import Board
from app.models.card import Card


@pytest.fixture
def app():
    # create the app with a test config dictionary
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    # close and remove the temporary database
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

# This fixture creates one board and saves it in the database
@pytest.fixture
def one_board_no_cards(app):
    new_board = Board(
        title="Winter", owner= "Lili"
    )
    db.session.add(new_board)
    db.session.commit()

# This fixture creates one board with two cards and saves it in the database
@pytest.fixture
def one_board_two_cards(app):
    card_1 = {
            "board_id": 1,
            "card_id": 1,
            "likes_count": 0,
            "message": "The woods are lovely, dark and deep..."
        }
    card_2 = {
            "board_id": 1,
            "card_id": 2,
            "likes_count": 0,
            "message": "Las ramas de los árboles están envueltas en fundas de hielo."
        }
    new_board = Board(
        title="Winter", 
        owner= "Lili",
        board_id=1,
        cards=[{
            "board_id": 1,
            "card_id": 1,
            "likes_count": 0,
            "message": "The woods are lovely, dark and deep..."
        },{
            "board_id": 1,
            "card_id": 2,
            "likes_count": 0,
            "message": "Las ramas de los árboles están envueltas en fundas de hielo."
        }]
    )
    db.session.add(new_board)
    db.session.commit()


    client.post("/boards/1/cards", request_body_1)
    client.post("/boards/1/cards", request_body_2)

# This fixture creates two boards with no cards and saves them in the database
@pytest.fixture
def two_boards_no_cards(app, one_board_no_cards):
    new_board = Board(
        title="Spring", owner="Adriana"
    )
    db.session.add(new_board)
    db.session.commit()