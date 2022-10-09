from typing import Dict, List, KeysView


class Table:
    def __display_meta_data(self, table_name: str) -> str:
        header = f"{table_name} Columns"
        print(header)
        print("-" * len(header))
        return header

    def display_data_in_tabular_form_for_columns(
        self, data: Dict, table_name: str
    ) -> None:
        self.__display_meta_data(table_name)

        if len(data) > 0:
            for value, data_type in data.items():
                print(f"{value} --> {data_type.__name__}")
        else:
            print("No results found. \n")

    def display_data_in_tabular_form_for_search(
        self, data: List, table_name: str
    ) -> None:
        header = self.__display_meta_data(table_name)

        if len(data) > 0:
            for row in data:
                for key, value in row.items():
                    print(f"{key}:  {value}")
                print("-" * len(header))
        else:
            print("No results found. \n")
