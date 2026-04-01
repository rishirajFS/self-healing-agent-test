# tests/fixtures/buggy_service.py
# This file was created by test_seed.py for pipeline testing.

def get_user_profile(data: dict) -> dict:
    """Return a user profile dict from a raw data payload."""
    uid = data.get("user_id", "")  # Fixed: safe default avoids KeyError
    return {"id": uid, "active": True}
