import csv


class Data:
    count_id = 0

    def __init__(self, year, month, data_field, value):
        Data.count_id += 1
        self.__data_id = Data.count_id
        self.__year = year
        self.__month = month
        self.__data_field = data_field
        self.__value = value

    # Accessor
    def get_data_id(self):
        return self.__data_id

    def get_data_field(self):
        return self.__data_field

    def get_year(self):
        return self.__year

    def get_month(self):
        return self.__month

    def get_value(self):
        return self.__value

    # Mutator Methods
    def set_data_id(self, data_id):
        self.__data_id = data_id

    def set_data_field(self, data_field):
        self.__data_field = data_field

    def set_year(self, year):
        self.__year = year

    def set_month(self, month):
        self.__month = month

    def set_value(self, value):
        self.__value = value


def read_csv():
    campaign_costs_dict = {}
    Inv_storage_costs_dict = {}
    UCE_costs_dict = {}
    UCW_costs_dict = {}
    admin_costs_dict = {}
    try:
        with open("costs.csv", "r") as data_file:
            data_reader = csv.DictReader(data_file)
            for line in data_reader:
                cc_data_object = Data(line["Year"], line["Month"], "Campaign Costs", line["Campaign Costs"])
                campaign_costs_dict[cc_data_object.get_data_id()] = cc_data_object

                ISC_data_object = Data(line["Year"], line["Month"], "Inventory Storage Costs", line["Inventory Storage Costs"])
                Inv_storage_costs_dict[ISC_data_object.get_data_id()] = ISC_data_object

                UCE_data_object = Data(line["Year"], line["Month"], "Utilities Costs: Electricity", line["Utilities Costs: Electricity"])
                UCE_costs_dict[UCE_data_object.get_data_id()] = UCE_data_object

                UCW_data_object = Data(line["Year"], line["Month"], "Utilities Costs: Water", line["Utilities Cost: Water"])
                UCW_costs_dict[UCW_data_object.get_data_id()] = UCW_data_object

                AC_data_object = Data(line["Year"], line["Month"], "Administration Costs", line["Administration Costs"])
                admin_costs_dict[AC_data_object.get_data_id()] = AC_data_object

    except FileNotFoundError:
        print("File not Found!")

    print(campaign_costs_dict)
    print(Inv_storage_costs_dict)
    print(UCE_costs_dict)
    print(UCW_costs_dict)
    print(admin_costs_dict)


read_csv()

