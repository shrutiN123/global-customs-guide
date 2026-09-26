from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

with open("data/customs_data.json", "r", encoding="utf-8") as file:
    customs_data = json.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/countries")
def countries():
    return jsonify(list(customs_data.keys()))


@app.route("/api/customs/<country>")
def get_customs(country):

    if country not in customs_data:
        return jsonify({"error": "Country not found"}), 404

    return jsonify(customs_data[country])


if __name__ == "__main__":
    app.run(debug=True)
