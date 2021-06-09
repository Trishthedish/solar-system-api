def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# GET /planets/1 returns a response body that matches our fixture
def test_get_one_planet(client, two_saved_planets):
  # act
  response = client.get("/planets/1")
  response_body = response.get_json()
  assert response.status_code == 200
  assert response_body == {
    "id": 1, 
    "name": "Venus", 
    "description": "big, red",
    "size": 55
  }

# GET /planets/1 with no data in test database (no fixture) returns a 404
def test_get_one_planet_without_data_returns_404(client):
  response = client.get("/planets/22")
  response_body = response.get_json()

  assert response_body == None
  assert response.status_code == 404

# GET /planets with valid test data (fixtures) returns a 200 with an array including appropriate test data


# POST /planets with a JSON request body returns a 201