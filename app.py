from crypt import methods
from operator import methodcaller
from flask import Flask, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template ('index.html')



# Error handling
@app.errorhandler(404)
def handle_404(err):
    return render_template('errors/404.html'), 404

@app.errorhandler(405)
def handle_405(err):
    return render_template('errors/405.html'), 405


@app.errorhandler(500)
def handle_500(err):
    return render_template('errors/500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)
