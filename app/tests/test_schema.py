import pytest
from app.schema import Schema


def test_schema_with_valid_input() -> None:
    input_string = "users"
    instance = Schema()
    expected_dict = {
        "_id": int,
        "url": str,
        "external_id": str,
        "name": str,
        "alias": str,
        "created_at": str,
        "active": bool,
        "verified": bool,
        "shared": bool,
        "locale": str,
        "timezone": str,
        "last_login_at": str,
        "email": str,
        "phone": str,
        "signature": str,
        "organization_id": int,
        "tags": list,
        "suspended": bool,
        "role": str,
    }

    resp = instance.get_schema(input_string)
    assert expected_dict == resp


def test_schema_with_invalid_input() -> None:
    input_string = "hello"
    instance = Schema()

    with pytest.raises(KeyError):
        instance.get_schema(input_string)
