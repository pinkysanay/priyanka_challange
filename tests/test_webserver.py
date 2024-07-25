import requests

def test_index_page():
    response = requests.get('http://example.com')
    assert response.status_code == 200
    assert "Hello World" in response.text

def test_https_redirect():
    response = requests.get('http://example.com', allow_redirects=False)
    assert response.status_code == 301
    assert response.headers['Location'] == 'https://example.com/'
