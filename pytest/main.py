import requests
import json

def test_create_user():
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    }
    response = requests.post('http://localhost:5000/users', headers=headers, data=json.dumps(data))
    assert response.status_code == 201
    response_data = response.json()
    assert response_data['username'] == 'testuser'
    assert response_data['email'] == 'testuser@example.com'
    assert 'id' in response_data

def test_get_user():
    response = requests.get('http://localhost:5000/users/1')
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['username'] == 'testuser'
    assert response_data['email'] == 'testuser@example.com'
    assert response_data['id'] == 1

def test_update_user():
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'username': 'updateduser',
        'email': 'updateduser@example.com',
        'password': 'password456'
    }
    response = requests.put('http://localhost:5000/users/1', headers=headers, data=json.dumps(data))
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['username'] == 'updateduser'
    assert response_data['email'] == 'updateduser@example.com'
    assert response_data['id'] == 1

def test_delete_user():
    response = requests.delete('http://localhost:5000/users/1')
    assert response.status_code == 204

def test_get_missing_user():
    response = requests.get('http://localhost:5000/users/1')
    assert response.status_code == 404
    assert response.json() == {'error': 'user not found'}