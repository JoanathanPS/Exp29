"""EX29 - Simple login function."""

# Demo in-memory user store: username -> password (plaintext ONLY for this
# lab demo -- never do this in a real app; use hashing e.g. bcrypt/argon2).
USERS = {
    "admin": "admin123",
    "joanathan": "csa1016",
}


def login(username, password):
    """Return True if username/password match a known user."""
    return USERS.get(username) == password


if __name__ == "__main__":
    print(login("joanathan", "csa1016"))   # True
    print(login("joanathan", "wrongpass")) # False
