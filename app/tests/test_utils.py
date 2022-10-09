# AAA(Arrange, Act, Assert)
import pytest
from app.utils import UserInputValidator, Base


class TestInputValidator:
    def test_user_input_number_with_valid_number(self) -> None:
        input_number = 1
        valid_range = [1, 2, 3]

        resp = UserInputValidator().validate_user_input_number(
            input_number, valid_range
        )

        assert resp == input_number

    def test_user_input_number_with_invalid_number(self) -> None:
        invalid_input_number = 4
        valid_range = [1, 2, 3]

        with pytest.raises(KeyError):
            UserInputValidator.validate_user_input_number(
                invalid_input_number, valid_range
            )

    def test_user_input_with_invalid_data_type(self) -> None:
        invalid_data_type = "hello"
        valid_range = [1, 2, 3]

        with pytest.raises(KeyError):
            UserInputValidator.validate_user_input_number(invalid_data_type, valid_range)  # type: ignore

    def test_search_term_with_valid_input(self) -> None:
        accepted_column_name = [
            "_id",
            "url",
            "external_id",
            "name",
            "alias",
            "created_at",
            "active",
            "verified",
            "shared",
            "locale",
            "timezone",
            "last_login_at",
            "email",
            "phone",
            "signature",
            "organization_id",
            "tags",
            "suspended" "role",
        ]
        input_string = "_id"

        resp = UserInputValidator.validate_search_term(input_string, accepted_column_name)  # type: ignore

        assert resp == input_string

    def test_search_term_with_invalid_input(self) -> None:
        accepted_column_name = [
            "_id",
            "url",
            "external_id",
            "name",
            "alias",
            "created_at",
            "active",
            "verified",
            "shared",
            "locale",
            "timezone",
            "last_login_at",
            "email",
            "phone",
            "signature",
            "organization_id",
            "tags",
            "suspended" "role",
        ]
        input_string = "hello"

        with pytest.raises(KeyError):
            UserInputValidator.validate_search_term(input_string, accepted_column_name)  # type: ignore

    def test_search_term_with_invalid_data_type(self) -> None:
        accepted_column_name = [
            "_id",
            "url",
            "external_id",
            "name",
            "alias",
            "created_at",
            "active",
            "verified",
            "shared",
            "locale",
            "timezone",
            "last_login_at",
            "email",
            "phone",
            "signature",
            "organization_id",
            "tags",
            "suspended" "role",
        ]
        input_number = 2

        with pytest.raises(KeyError):
            UserInputValidator.validate_search_term(input_number, accepted_column_name)  # type: ignore


class TestBase:
    def test_get_type_conversion_based_on_schema_with_valid_data(self) -> None:
        file_name = "users"
        search_term = "_id"
        search_value = "1"

        instance = Base()
        value, data_type = instance.get_type_conversion_based_on_schema(
            search_term, search_value, file_name
        )

        assert data_type == int
        assert value == 1

    def test_get_type_conversion_based_on_schema_with_invalid_data_type(self) -> None:
        file_name = "users"
        search_term = 12
        search_value = "1"

        instance = Base()

        with pytest.raises(KeyError):
            instance.get_type_conversion_based_on_schema(search_term, search_value, file_name)  # type: ignore

    def test_get_filtered_data_with_data_type_as_list(self) -> None:
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
        search_term = "tags"
        search_value = "Sutton"
        data_type = list

        instance = Base()
        resp = instance.get_filtered_data(data, search_term, search_value, data_type)

        assert type(resp) == list
        assert len(resp) == 1

    def test_get_filtered_data_with_data_type_as_int(self) -> None:
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
        search_term = "_id"
        search_value = 1
        data_type = int

        instance = Base()
        resp = instance.get_filtered_data(data, search_term, search_value, data_type)

        assert type(resp) == list
        assert len(resp) == 1

    def test_get_filtered_data_with_data_type_as_bool(self) -> None:
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
        search_term = "active"
        search_value = True
        data_type = bool

        instance = Base()
        resp = instance.get_filtered_data(data, search_term, search_value, data_type)

        assert type(resp) == list
        assert len(resp) == 1

    def test_get_filtered_data_with_non_existing_id(self) -> None:
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
        search_term = "_id"
        search_value = 300
        data_type = int

        instance = Base()
        resp = instance.get_filtered_data(data, search_term, search_value, data_type)

        assert type(resp) == list
        assert len(resp) == 0

    def test_get_json_file_data_with_valid_file_name(self) -> None:
        file_name = "users"

        instance = Base()
        resp = instance.get_json_file_data(file_name)

        assert type(resp) == list

    def test_get_json_file_data_with_invalid_file_name(self) -> None:
        file_name = "invalid_file_name"

        instance = Base()

        with pytest.raises(FileNotFoundError):
            instance.get_json_file_data(file_name)

    def test_convert_data_type_with_bool_data(self) -> None:
        data_type = bool
        value = "true"

        instance = Base()
        resp = instance.convert_data_type(data_type, value)

        assert type(resp) == bool

    def test_convert_data_type_with_list_data(self) -> None:
        data_type = list
        value = "Springville"

        instance = Base()
        resp = instance.convert_data_type(data_type, value)

        assert type(resp) == str

    def test_convert_data_type_with_int_data(self) -> None:
        data_type = int
        value = "1"

        instance = Base()
        resp = instance.convert_data_type(data_type, value)

        assert type(resp) == int

    def test_convert_data_type_with_invalid_data(self) -> None:
        data_type = bool
        value = 1122

        instance = Base()

        with pytest.raises(AttributeError):
            instance.convert_data_type(data_type, value)
