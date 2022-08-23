from crypt import methods
from operator import methodcaller
from flask import Flask, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

# Database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Connect sql db to heroku

# class Model
class URLModel(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.string())
    short_id = db.Column(db.String())

    def __init__(self, url, short_id):
        self.url = url
        self.short_id = short_id

    def __repr__(self) -> str:
        return f"<URL: {self.url}"



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
