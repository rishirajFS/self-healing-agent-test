# tests/fixtures/buggy_service.py
# This file was created by test_seed.py for pipeline testing.

def get_user_profile(data: dict) -> dict:
    """Return a user profile dict from a raw data payload."""
    uid = data["user_id"]   # Bug: raises KeyError when user_id is absent
    return {"id": uid, "active": True}
