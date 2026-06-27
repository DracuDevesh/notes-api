from app.services.user_service import (
    hash_password,
    verify_password
)

hashed = hash_password("hello123")

print(hashed)

print(
    verify_password(
        "hello123",
        hashed
    )
)

print(
    verify_password(
        "wrongpassword",
        hashed
    )
)