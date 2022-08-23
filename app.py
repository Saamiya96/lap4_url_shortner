from flask import Flask, request, jsonify, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from werkzeug import exceptions
import string
import random

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

db.create_all()

@app.route('/', methods=['GET', 'POST'])
def url_handler():
    if request.method == 'POST':
        url = request.form['url']
        check_url = URLModel.query.filter_by(url=url).first()
        
        if not url:
            return render_template('index.html',text='You need to enter a URL!'), 200
        
        if check_url:
            short_id=check_url.short_id
            return render_template('index.html',text='That URL already has a link:', link=request.host_url + short_id), 200
       
        short_id = create_short_id(6)

        new_url = URLModel(
            url=url, short_id=short_id)
        db.session.add(new_url)
        db.session.commit()
        

        return render_template('index.html', text= "Here is your new URL:", link=request.host_url + short_id)
         
    return render_template('index.html')



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
