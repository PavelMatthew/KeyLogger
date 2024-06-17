import json
from pprint import pprint
from userdata import UserData
import os

class FileWork:

    def __init__(self, our_user):
        self.file_name = "data.json"
        self.our_user = our_user

    @staticmethod
    def read_file():
        with open("data.json", "r", encoding='utf-8') as file:
            return json.load(file)

    def write_to_file(self):

        try:

            if os.stat(self.file_name).st_size > 0:
                print("here")
                n_data = self.read_file()
                n_data['users'].append(self.our_user.__dict__)
                with open(self.file_name, "w", encoding='utf-8') as file:
                    json.dump(n_data, file, indent=8)

            else:
                data = {
                    "users": []
                }
                data['users'].append(self.our_user.__dict__)
                with open(self.file_name, "w", encoding='utf-8') as file:
                    json.dump(data, file, indent=8)
        except OSError:
            print("No file")







