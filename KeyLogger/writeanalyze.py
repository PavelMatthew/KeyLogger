import json
from pprint import pprint
from userdata import UserData
import os

class WriteAnalyze:
    
    def __init__(self, our_user):
        self.file_name = "analyze.json"
        self.our_user = our_user

    @staticmethod
    def read_file():
        with open("analyze.json", "r", encoding='utf-8') as file:
            return json.load(file)

    def write_to_file(self):

        try:

            data = {
                  "users": []
            }
            data['users'].append(self.our_user.__dict__)

            with open(self.file_name, "w", encoding='utf-8') as file:
                json.dump(data, file, indent=8)
        except OSError:
            print("No file")

