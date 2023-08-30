#!/usr/bin/python3
from main import app
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_login_post(client):
    response = client.post("/", data={"email": "test@example.com", "password": "password"})
    assert response.status_code == 200
'''def test_home_no_user_input(client):
    # Simulate a logged-in session
        session['logged_in'] = True
        session['email'] = 'dap@mail.com.com'
        assert b'Please enter your name and quote' in response.data
    response = client.post('/home', data={})
    print(response.data)  # Print the response data
    assert b'Please enter your name and quote' in response.data
'''    
