from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from RG_manual_upload import ManualUploadForm
import csv
import datetime
from costs import Data
from random import sample

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

                ISC_data_object = Data(line["Year"], line["Month"], "Inventory Storage Costs",
                                       line["Inventory Storage Costs"])
                Inv_storage_costs_dict[ISC_data_object.get_data_id()] = ISC_data_object

                UCE_data_object = Data(line["Year"], line["Month"], "Utilities Costs: Electricity",
                                       line["Utilities Costs: Electricity"])
                UCE_costs_dict[UCE_data_object.get_data_id()] = UCE_data_object

                UCW_data_object = Data(line["Year"], line["Month"], "Utilities Costs: Water",
                                       line["Utilities Cost: Water"])
                UCW_costs_dict[UCW_data_object.get_data_id()] = UCW_data_object

                AC_data_object = Data(line["Year"], line["Month"], "Administration Costs", line["Administration Costs"])
                admin_costs_dict[AC_data_object.get_data_id()] = AC_data_object

    except FileNotFoundError:
        print("File not Found!")

    now = datetime.datetime.now()

    data_sent = []
    for key, value in campaign_costs_dict.items():
        cc = campaign_costs_dict[key].get_data_id()
        if now.year == int(value.get_year()):
            data = [cc, value.get_year(), value.get_month(), value.get_data_field(), value.get_value()]
            data_sent.append(data)

    value = []
    for result in data_sent:
        hi = [result[2], result[4]]
        value.append(hi)

    return render_template('RG/cost_analysis.html', data=value)


@app.route('/data')
def data():
    return jsonify({'results': sample(range(1, 10), 5)})


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
