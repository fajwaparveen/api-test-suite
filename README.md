# API Test Suite

Automated API tests written with Python, Pytest and requests

## What it tests

- Status codes (200,201,404)
- Response data (fields and values)
- Negative cases (missing and invalid ids)
- Boundary values (ids 0,1,100,101,-1)
- Create,read,update and delete requests

## How to run

pip install -r requirements.txt
pytest -v

## HTML report

pytest --html=report.html --self-contained-html

## Tech

Python, PyTest, requests, pytest-html
Tested against the JSONPlaceholder practice API
