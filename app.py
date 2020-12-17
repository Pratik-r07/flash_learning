# app.py

# Import the Flask class (for the main app)
# Import render_templates to run routes based on templates
# Import url_for in order to link stylesheets in the base jinja2 template
from flask import Flask, render_template, url_for

# Starts a new Flask app using this app file
app = Flask(__name__)

# Start a new route for the index page
@app.route('/')
def index():

	# User render templates to use the index.html file as a template for the index page
	return render_template('index.html')

# When app is run, start the Flask app on the localhost server (port 5000)
if __name__ == "__main__":
	app.run(debug=True)