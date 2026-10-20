import pytest
import requests


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture
def post_response(base_url):
    return requests.get(base_url + "/posts/1")
