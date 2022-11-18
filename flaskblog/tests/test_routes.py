from flaskblog.models import User
from flaskblog import create_app


# route unit tests

def test_index_success(client):
  # Page loads
  response = client.get('/')
  assert response.status_code == 200

def test_about_success(client):
  # Page loads
  response = client.get('/about')
  assert response.status_code == 200

def test_register_router_success(client):
  # Page loads
  response = client.post('/register')
  assert response.status_code == 200

def test_login_route_success(client):
  # Page loads
  response = client.post('/login')
  assert response.status_code == 200


# functional test

def test_home_page():
    flask_app = create_app("flask_test.cfg")

    with flask_app.test_client() as test_client:
        response = test_client.post("/")
        assert response.status_code == 405
        assert b"Flask User Management Example" not in response.data
        assert b"Need an account" not in response.data
    



# def test_empty_db(client):
#     """Start with a blank database."""
#     rv = client.get('/')
#     assert b'No entries here so far' in rv.data


# def test_new_user():
#     user = User("ben", "ben@gmx.de", "password")

#     assert user.email == "ben@gmx.de"
#     assert user.password != "password"
