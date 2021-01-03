import pandas as pd
import csv
from collections import defaultdict


# class Data:
#     import_csv = 0
#
#     def __init__(self, data_field, year, month, value):
#         Data.import_csv += 1
#         self.__data_field = data_field
#         self.__year = year
#         self.__month = month
#         self.__value = value
#
#     # Accessor
#     def get_data_field(self):
#         return self.__data_field
#
#     def get_year(self):
#         return self.__year
#
#     def get_month(self):
#         return self.__month
#
#     def get_value(self):
#         return self.__value
#
#     # Mutator Methods
#     def set_data_field(self, data_field):
#         self.__data_field = data_field
#
#     def set_year(self, year):
#         self.__year = year
#
#     def set_month(self, month):
#         self.__month = month
#
#     def set_value(self, value):
#         self.__value = value

df = pd.read_csv("costs.csv")
saved_column = df["Campaign Costs"]
print(saved_column)
