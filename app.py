from flask import Flask, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template ('index.html')

if __name__ == "__main__":
    app.run(debug=True)
