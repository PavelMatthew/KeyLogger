import os

class FileWork:

    def __init__(self, user_name, text, num_mistake, middle_time_pressed, middle_speed, middle_spead_without_big_pauses, dict_symbols, dict_pauses):
        self.file_name = "data"


    def write_to_file(self):
        with open("data.txt", "a", encoding='utf-8') as myfile:
            myfile.write("\nВсё ОК")


if __name__ == "__main__":
    pass