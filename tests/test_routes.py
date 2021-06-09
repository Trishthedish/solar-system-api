def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []
    
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