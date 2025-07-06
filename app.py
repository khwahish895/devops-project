from flask import Flask
 
app = Flask(__name__)

@app.route("/info")
def lwinfo():
	return "I am lw from India"

@app.route("/phone")
def lwphone():
	return"7424988589"
app.run(host="0.0.0.0")

	