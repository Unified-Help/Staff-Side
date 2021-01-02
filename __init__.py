from flask import Flask, render_template, request, redirect, url_for, session

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
    return render_template('RG/cost_analysis.html')


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
    return render_template('RG/manual_insertForm.html')


# ------------ Error Handling------------ #
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


if __name__ == '__main__':
    app.run()
