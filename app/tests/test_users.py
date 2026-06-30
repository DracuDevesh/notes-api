from uuid import uuid4


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to Notes API"
    }


def test_register_user(client):
    payload = {
        "username": f"user_{uuid4().hex[:8]}",
        "email": f"{uuid4().hex[:8]}@test.com",
        "password": "Password123"
    }

    response = client.post(
        "/users/register",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]
    assert "hashed_password" not in data


def test_login_user(client):
    username = f"user_{uuid4().hex[:8]}"
    email = f"{uuid4().hex[:8]}@test.com"
    password = "Password123"

    client.post(
        "/users/register",
        json={
            "username": username,
            "email": email,
            "password": password
        }
    )

    response = client.post(
        "/users/login",
        data={
            "username": email,
            "password": password
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"