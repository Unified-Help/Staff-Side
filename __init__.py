from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from RG_manual_upload import ManualUploadForm
import csv
import datetime
from costs import Data

app = Flask(__name__)
app.secret_key = 'any_random_string'


@app.route('/')
def home():
    return render_template('home.html', user_name="General Kenobi")


# ------------ Account Management ------------ #
@app.route("/staff_profile")
def staff_profile():
    return render_template('AM/staff_profile.html')


@app.route("/account_management")
def account_management():
    return render_template('AM/unlock_delete_acc.html')


# ------------ Transaction Processing ------------ #

@app.route("/incoming_items")
def incoming_item():
    return render_template('TP/incoming_item.html')


# ------------ Customer Support ------------ #

@app.route("/forum_FAQ")
def forum_FAQ():
    return render_template('CS/forum_FAQ.html')


# ------------ Report Generation ------------ #

@app.route("/dashboard")
def dashboard():
    return render_template('RG/dashboard.html')


@app.route("/cost_analysis")
def cost_analysis():
    # Dictionaries for different costs. Helps with data management and also reduces complexity
    campaign_costs_dict = {}
    Inv_storage_costs_dict = {}
    UCE_costs_dict = {}
    UCW_costs_dict = {}
    admin_costs_dict = {}
    try:
        with open("costs.csv", "r") as data_file:
            # Converts each line from the csv file into a dictionary. For example, the first line, as a dictionary, will be,
            # {'Year': '2015', 'Month': 'JAN', 'Campaign Costs': '3992', 'Inventory Storage Costs': '1217', 'Utilities Costs: Electricity': '305', 'Utilities Cost: Water': '440', 'Administration Costs': '5782'}
            # Therefore, the key is the heading of each column and the value is the corresponding data value of that column and row
            data_reader = csv.DictReader(data_file)
            for line in data_reader:
                # Creates object for campaign cost value in the line with "Data" class.
                cc_data_object = Data(line["Year"], line["Month"], "Campaign Costs", line["Campaign Costs"])
                # Stores the object in the respective dictionary using the data_id of object as the key.
                campaign_costs_dict[cc_data_object.get_data_id()] = cc_data_object

                # Creates object for inventory storage cost value in the line with "Data" class.
                ISC_data_object = Data(line["Year"], line["Month"], "Inventory Storage Costs",
                                       line["Inventory Storage Costs"])
                # Stores the object in the respective dictionary using the data_id of object as the key.
                Inv_storage_costs_dict[ISC_data_object.get_data_id()] = ISC_data_object

                # Creates object for UCE cost value in the line with "Data" class.
                UCE_data_object = Data(line["Year"], line["Month"], "Utilities Costs: Electricity",
                                       line["Utilities Costs: Electricity"])
                # Stores the object in the respective dictionary using the data_id of object as the key.
                UCE_costs_dict[UCE_data_object.get_data_id()] = UCE_data_object

                # Creates object for UCW cost value in the line with "Data" class.
                UCW_data_object = Data(line["Year"], line["Month"], "Utilities Costs: Water",
                                       line["Utilities Cost: Water"])
                # Stores the object in the respective dictionary using the data_id of object as the key.
                UCW_costs_dict[UCW_data_object.get_data_id()] = UCW_data_object

                # Creates object for administration cost value in the line with "Data" class.
                AC_data_object = Data(line["Year"], line["Month"], "Administration Costs", line["Administration Costs"])
                # Stores the object in the respective dictionary using the data_id of object as the key.
                admin_costs_dict[AC_data_object.get_data_id()] = AC_data_object

    # Error exceptions
    except FileNotFoundError:
        print("File not Found!")

    except:
        print("Error in extracting data from file. "
              "Ensure that the headings and index of file uploaded matches the template file.")

    # Utilises the datetime module calls the now function which gets the current year,month,week,day and exact time.
    # This is later used to get the current year. It is needed to show data from different time frames.
    now = datetime.datetime.now()

    # ========== Retrieve ==========
    chart_data = []
    for key, value in campaign_costs_dict.items():
        cc = campaign_costs_dict[key].get_data_id()
        if now.year - 1 == int(value.get_year()):
            data = [value.get_month(), value.get_value()]
            chart_data.append(data)

    return render_template('RG/cost_analysis.html', data=chart_data)


@app.route("/upload_insert_data")
def upload_insert_data():
    return render_template('RG/upload_insert_data.html')


@app.route("/detailed_analysis")
def detailed_analysis():
    return render_template('RG/detailed_analysis.html')


@app.route("/upload_dataForm")
def upload_dataForm():
    return render_template('RG/upload_dataForm.html')


@app.route("/manual_insertForm")
def manual_insertForm():
    # manual_upload_form = ManualUploadForm(request.form)
    # if request.method == 'POST' and manual_upload_form.validate()

    return render_template('RG/manual_insertForm.html')


# ------------ Error Handling------------ #
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
