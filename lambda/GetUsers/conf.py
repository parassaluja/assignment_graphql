import os
import json


class Conf():

    def __init__(self):

        param = self.get_param()

    def get_param(self):
        try:
            with open(os.path.join(os.path.dirname(__file__), 'param.json')) as json_data_file:
            #with open('pb_param.json') as json_data_file:
                json_param = json.load(json_data_file)
            return json_param
        except Exception as e:
            print("*********** Exception in parameters file ********", e)

