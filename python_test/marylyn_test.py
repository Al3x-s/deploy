import pytest
import re
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_valid_email_input(client):
    valid_email = 'valid@example.com'
    response = client.post('/', data={'email': valid_email, 'password': 'password'}, follow_redirects=True)
    
    assert b'User Cards' in response.data

    # Validate email format
    assert re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', valid_email) is not None

