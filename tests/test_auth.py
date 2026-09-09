def test_login(client):
    response = client.post(
        "/login",
        data={
            "username": "darshan",
            "password": "1qaz2wsx"
        }
    )

    assert response.status_code == 200
def test_login_wrong_password(client):
    response = client.post(
        "/login",
        data={
            "username": "testuser",
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 401