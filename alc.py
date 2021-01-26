from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///new.db"

db=SQLAlchemy(app)
class login(db.Model):
    email=db.Column('db.Text',primary_key=True)
                    
                    
    def __repr__(self):
        return "new mail" + str(self.email)    

email="newsjdasksa.com"
