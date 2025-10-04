import requests, pytest

@pytest.fixture(scope="session")
def token(base_url):
    r = requests.post(f"{base_url}/auth", json={"username":"admin","password":"password123"})
    assert r.status_code == 200
    return r.json()["token"]

def _new_payload(first="Reni", last="Tester"):
    return {
        "firstname": first,
        "lastname": last,
        "totalprice": 123,
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-10-10", "checkout": "2025-10-12"},
        "additionalneeds": "Breakfast"
    }

def test_booking_crud_happy_path(base_url, token):
    # Create
    resp = requests.post(f"{base_url}/booking", json=_new_payload())
    assert resp.status_code == 200
    booking_id = resp.json()["bookingid"]

    # Read
    got = requests.get(f"{base_url}/booking/{booking_id}")
    assert got.status_code == 200
    assert got.json()["firstname"] == "Reni"

    # Update (requires auth cookie)
    upd = _new_payload(first="Reniya")
    put = requests.put(
        f"{base_url}/booking/{booking_id}",
        json=upd,
        headers={"Cookie": f"token={token}", "Content-Type": "application/json"}
    )
    assert put.status_code == 200
    assert put.json()["firstname"] == "Reniya"

    # Delete
    dele = requests.delete(f"{base_url}/booking/{booking_id}", headers={"Cookie": f"token={token}"})
    assert dele.status_code in [200, 201, 204]  # API kadang return 201
    # Verify deleted
    check = requests.get(f"{base_url}/booking/{booking_id}")
    assert check.status_code == 404

def test_update_with_invalid_token_forbidden(base_url):
    # create booking dulu tanpa token
    resp = requests.post(f"{base_url}/booking", json=_new_payload(first="Temp"))
    assert resp.status_code == 200
    bid = resp.json()["bookingid"]

    # coba update pakai token salah -> 403
    bad = requests.put(
        f"{base_url}/booking/{bid}",
        json=_new_payload(first="Hacked"),
        headers={"Cookie": "token=invalid", "Content-Type":"application/json"}
    )
    assert bad.status_code == 403
