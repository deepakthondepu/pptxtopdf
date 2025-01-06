import os
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_convert_endpoint_no_file(client):
    response = client.post('/convert')
    assert response.status_code == 400
    assert response.json['error'] == "No file provided"

def test_convert_endpoint_invalid_file(client):
    data = {'file': (b"This is not a PPTX file", "test.txt")}
    response = client.post('/convert', data=data, content_type='multipart/form-data')
    assert response.status_code == 400
    assert response.json['error'] == "File must be a .pptx file"

def test_convert_endpoint_valid_file(client):
    test_pptx_path = 'tests/sample.pptx'

    if not os.path.exists('tests'):
        os.makedirs('tests')
    with open(test_pptx_path, 'wb') as f:ven
        f.write(b"Fake PPTX content for testing")

    with open(test_pptx_path, 'rb') as f:
        data = {'file': (f, 'sample.pptx')}
        response = client.post('/convert', data=data, content_type='multipart/form-data')
   
    assert response.status_code == 200
    assert response.content_type == 'application/pdf'

    os.remove(test_pptx_path)