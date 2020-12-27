# Staff-Side
If you need to add/remove/change links in sidebar/navbar, just look for the comments. The line below the comments is where you will be able to make your necessary changes.

Make sure to "pip install dash" before running staff-side __init__. It will take about two minutes.

If you want to make a new HTML file that extends “base.html”, copy paste the following code into the new html file:

{% extends "/base.html" %}

{% block title %} Unified Help - Account Management{% endblock %}

<!-- Any css files/ internal css in here -->
{% block head %}
{{ super() }}
{% endblock %}

<!-- Page content in here -->
{% block content %}
{% endblock %}

<!-- Link any js files here -->
{% block script %}
{{ super() }}
{% endblock %}

!!!! Do not remove “{{  super()  }}”, just put your relevant files below it
After creating your html file, make sure to put it in the correct folder and make the necessary links

•	All css/js files in “static”
•	All html files in “templates”
•	All python files in “Python”
