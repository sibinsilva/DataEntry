from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
import uuid

file_path = os.path.abspath(os.getcwd())+"\\WebPage\\Database\\formDB.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path  # SQLite database file path
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    dob = db.Column(db.Date)
    gender = db.Column(db.String(10))
    address1 = db.Column(db.String(100))
    address2 = db.Column(db.String(100))
    address3 = db.Column(db.String(100))
    address4 = db.Column(db.String(100))
    postcode = db.Column(db.String(20))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = str(uuid.uuid4())

@app.route('/', methods=['GET', 'POST'])
def registration_form():
    if request.method == 'POST':
        try:
            first_name = request.form['firstName']
            last_name = request.form['lastName']
            dob = datetime.strptime(request.form['dob'], '%Y-%m-%d').date()
            gender = request.form['gender']
            address1 = request.form['address1']
            address2 = request.form['address2']
            address3 = request.form['address3']
            address4 = request.form['address4']
            postcode = request.form['postcode']
            phone = request.form['phone']
            email = request.form['email']
            
            new_user = Users(first_name=first_name, last_name=last_name, dob=dob, gender=gender, address1=address1,
                            address2=address2, address3=address3, address4=address4, postcode=postcode,
                            phone=phone, email=email)
            db.session.add(new_user)
            db.session.commit()
            return 'User data saved successfully', 200
        except Exception as e:
            app.logger.error('An error occurred: %s', str(e))
            return 'An error occurred while saving user data', 500

    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
