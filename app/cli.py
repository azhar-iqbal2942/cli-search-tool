from app.constants import (
    WELCOME_TEXT,
    JSON_FILE_SELECTION_TEXT,
    SELECT_SEARCH_OR_VIEW_FIELDS_OF_SELECTED_FILE_TEXT,
    map_input_with_file,
)
from app.utils import Base


class SearchCommandLineInterface(Base):
    def search(self):
        exit_flag = True
        print(WELCOME_TEXT)

        while exit_flag:
            print(JSON_FILE_SELECTION_TEXT)
            try:
                search_option = self.validate_user_input_number(
                    int(input("Select options from above list: ")), [1, 2, 3]
                )

                selected_file = map_input_with_file[int(search_option)]
                data = self.get_json_file_data(selected_file)
                print(SELECT_SEARCH_OR_VIEW_FIELDS_OF_SELECTED_FILE_TEXT)
                selected_option = self.validate_user_input_number(
                    int(input("Enter Number: ")), [1, 2]
                )

                if selected_option == 1:
                    search_term = self.validate_search_term(
                        input("Enter search term: "), self.get_headers_of_file(data)
                    )
                    search_value = input("Enter search value: ")

                    (
                        converted_search_value,
                        data_type,
                    ) = self.get_type_conversion_based_on_schema(
                        search_term, search_value, selected_file
                    )
                    filtered_dict = self.get_filtered_data(
                        data, search_term, converted_search_value, data_type
                    )
                    self.display_data_in_tabular_form_for_search(
                        filtered_dict, selected_file
                    )
                else:
                    schema = self.get_schema(selected_file)
                    self.display_data_in_tabular_form_for_columns(schema, selected_file)
            except Exception as e:
                print(str(e))
                continue

            # take input whether user want's to continue or quit
            user_decision = input("Press Enter to Continue or type quit to exit: ")
            if user_decision.lower() == "quit":
                exit_flag = False
