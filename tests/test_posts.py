import requests
import pytest


def test_status_is_200(post_response):
    assert post_response.status_code == 200


def test_has_correct_data(post_response):
    data = post_response.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data


def test_nonexistent_post_returns_404(base_url):
    response = requests.get(base_url + "/posts/99999")
    assert response.status_code == 404


def test_invalid_post_id_returns_404(base_url):
    response = requests.get(base_url + "/posts/abc")
    assert response.status_code == 404


@pytest.mark.parametrize("post_id", [1,50,100])
def test_valid_post_ids_return_200(base_url, post_id):
    response = requests.get(base_url + "/posts/" + str(post_id))
    assert response.status_code == 200


@pytest.mark.parametrize("post_id", [-1,0,101])
def test_invalid_post_ids_return_404(base_url, post_id):
    response = requests.get(base_url + "/posts/" + str(post_id))
    assert response.status_code == 404


def test_create_returns_201(base_url):
    new_post = {"title": "My test post", "body": "Hello", "userId": 1}
    response = requests.post(base_url + "/posts", json=new_post)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "My test post"
    assert "id" in data 


def test_update_post_returns_200(base_url):
    updated = {"id": 1, "title": "New title", "body": "New body", "userId": 1}
    response = requests.put(base_url + "/posts/1", json=updated)
    assert response.status_code == 200
    assert response.json()["title"] == "New title"


def test_delete_post_returns_200(base_url):
    response = requests.delete(base_url + "/posts/1")
    assert response.status_code == 200
