import json
from typing import List, Dict, KeysView, Any

# Custom Imports
from app.schema import Schema
from app.table import Table


class UserInputValidator:
    @classmethod
    def validate_search_term(cls, search_term: str, data: KeysView[str]) -> str:
        if search_term not in data:
            raise KeyError("Search Term Not Found.")
        return search_term

    @classmethod
    def validate_user_input_number(cls, value: int, range_list: List) -> int:
        if value not in range_list:
            raise KeyError(f"Accepted value are {range_list}")
        return value


class Base(UserInputValidator, Schema, Table):
    def get_type_conversion_based_on_schema(
        self, search_term: str, search_value: str, file_name
    ) -> tuple:
        user_schema = self.get_schema(file_name)
        data_type = user_schema[search_term]
        return self.convert_data_type(data_type, search_value), data_type

    def get_headers_of_file(self, data: List) -> KeysView[str]:
        """
        Picking index 0 keys as the schema is same for the json file
        """
        return data[0].keys()

    def convert_data_type(self, data_type: Any, value: Any) -> Any:
        converted_value = None
        if data_type == bool:
            converted_value = eval(value.title())
        elif data_type == list:
            converted_value = value
        else:
            converted_value = data_type(value)

        return converted_value

    def get_json_file_data(self, file_name: str) -> List[Dict]:
        # Loading data in memeory because file is not very large.
        # if file size is huge than I will prefer to use pandas and process data in chunks.
        with open(f"./data/{file_name}.json", "r") as json_file:
            data = json.load(json_file)

        return data

    def get_filtered_data(
        self, data: List, search_term: str, search_value: Any, data_type: Any
    ) -> List[Dict | None]:

        if data_type == list:
            filtered_list = [
                obj for obj in data if str(search_value) in obj.get(search_term)
            ]
        else:
            filtered_list = [
                obj for obj in data if obj.get(search_term) == search_value
            ]

        return filtered_list
