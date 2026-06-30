from uuid import uuid4


def register_and_login(client):
    username = f"user_{uuid4().hex[:8]}"
    email = f"{uuid4().hex[:8]}@test.com"
    password = "Password123"

    client.post(
        "/users/register",
        json={
            "username": username,
            "email": email,
            "password": password,
        },
    )

    login = client.post(
        "/users/login",
        data={
            "username": email,
            "password": password,
        },
    )

    token = login.json()["access_token"]

    return {
        "Authorization": f"Bearer {token}"
    }


def test_notes_crud(client):
    headers = register_and_login(client)

    create = client.post(
        "/notes",
        headers=headers,
        json={
            "title": "FastAPI",
            "content": "Testing"
        },
    )

    assert create.status_code == 201

    note = create.json()

    note_id = note["id"]

    get_all = client.get(
        "/notes",
        headers=headers,
    )

    assert get_all.status_code == 200
    assert len(get_all.json()) == 1

    get_one = client.get(
        f"/notes/{note_id}",
        headers=headers,
    )

    assert get_one.status_code == 200

    update = client.put(
        f"/notes/{note_id}",
        headers=headers,
        json={
            "title": "Updated",
            "content": "Updated Content"
        },
    )

    assert update.status_code == 200

    delete = client.delete(
        f"/notes/{note_id}",
        headers=headers,
    )

    assert delete.status_code == 200

    final = client.get(
        "/notes",
        headers=headers,
    )

    assert final.json() == []