import pandas as pd
import csv
from collections import defaultdict


class Data:

    def __init__(self, data_field):
        self.__data_field = data_field
        self.__year = ""
        self.__month = ""
        self.__value = 0

    # Accessor
    def get_data_field(self):
        return self.__data_field

    def get_year(self):
        return self.__year

    def get_month(self):
        return self.__month

    def get_value(self):
        return self.__value

    # Mutator Methods
    def set_data_field(self, data_field):
        self.__data_field = data_field

    def set_year(self, year):
        self.__year = year

    def set_month(self, month):
        self.__month = month

    def set_value(self, value):
        self.__value = value


def read_csv():
    many_data = []
    try:
        df = pd.read_csv("costs.csv", index_col = "YYYY-MM")
        df_dict = df.to_dict()
        print(df_dict)
        for key in df_dict:
            for year_month,d_value in df_dict[key].items():
                data_info = Data(key)
                data_info.set_year(year_month[0:4])
                data_info.set_month(year_month[5:8])
                data_info.set_value(d_value)
                many_data.append(data_info)

    except FileNotFoundError:
        print("File not Found!")

    for s in many_data:
        print("{}, {}, {}, {}".format(s.get_data_field(), s.get_year(), s.get_month(), s.get_value()))


read_csv()
