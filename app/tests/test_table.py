import pytest
from app.table import Table
from app.schema import Schema


def test_display_data_in_tabular_form_for_columns_with_valid_data() -> None:
    table_name = "Users"
    data = Schema.get_schema("users")
    instance = Table()

    resp = instance.display_data_in_tabular_form_for_columns(data, table_name)  # type: ignore
    assert None == resp


def test_display_data_in_tabular_form_for_columns_with_empty_list() -> None:
    table_name = "Users"
    data = []
    instance = Table()

    resp = instance.display_data_in_tabular_form_for_columns(data, table_name)  # type: ignore
    assert None == resp


def test_display_data_in_tabular_form_for_columns_with_invalid_data_type() -> None:
    table_name = "Users"
    data = 123
    instance = Table()

    with pytest.raises(TypeError):
        instance.display_data_in_tabular_form_for_columns(data, table_name)  # type: ignore


def test_display_data_in_tabular_form_for_search_with_valid_data() -> None:
    table_name = "Users"
    data = [
        {
            "_id": 1,
            "url": "http://initech.aiworks.com/api/v2/users/1.json",
            "external_id": "74341f74-9c79-49d5-9611-87ef9b6eb75f",
            "name": "Francisca Rasmussen",
            "alias": "Miss Coffey",
            "created_at": "2016-04-15T05:19:46 -10:00",
            "active": True,
            "verified": True,
            "shared": True,
            "locale": "en-AU",
            "timezone": "Sri Lanka",
            "last_login_at": "2013-08-04T01:03:27 -10:00",
            "email": "coffeyrasmussen@flotonic.com",
            "phone": "8335-422-718",
            "signature": "Don't Worry Be Happy!",
            "organization_id": 119,
            "tags": ["Springville", "Sutton", "Hartsville/Hartley", "Diaperville"],
            "suspended": True,
            "role": "admin",
        }
    ]
    instance = Table()

    resp = instance.display_data_in_tabular_form_for_search(data, table_name)
    assert None == resp


def test_display_data_in_tabular_form_for_search_with_empty_list() -> None:
    table_name = "Users"
    data = []
    instance = Table()

    resp = instance.display_data_in_tabular_form_for_search(data, table_name)
    assert None == resp


def test_display_data_in_tabular_form_for_search_with_invalid_data_type() -> None:
    table_name = "Users"
    data = 123
    instance = Table()

    with pytest.raises(TypeError):
        instance.display_data_in_tabular_form_for_search(data, table_name)  # type: ignore
