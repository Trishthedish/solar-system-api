import pytest
from app import create_app
from app import db
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    venus = Planet(
      name="Venus", 
      description="big, red", 
      size=55
    )

    mars = Planet(
      name="Mars",
      description="no oxygen",
      size=44
    )

    db.session.add_all([venus,mars])
    db.session.commit()

    return app.test_client()
