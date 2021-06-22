import json


def test_index(app, client):
    response = client.get("/")
    assert response.status_code == 200
    expected = "Hello World!"
    assert expected == response.get_data(as_text=True)


def test_status(app, client):
    response = client.get("/status")
    assert response.status_code == 200
    expected = {"user": "admin", "result": "OK - healthy"}
    assert expected == json.loads(response.get_data(as_text=True))


def test_metrics(app, client):
    response = client.get("/metrics")
    assert response.status_code == 200
    expected = {
        "status": "success",
        "code": 0,
        "data": {"UserCount": 140, "UserCountActive": 23},
    }
    assert expected == json.loads(response.get_data(as_text=True))
