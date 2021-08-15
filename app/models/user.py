
#------------------WAVE 1-------------------------------------------
from app import db 

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True)
    user_full_name = db.Column(db.String)
    user_address = db.Column(db.String)
    user_phone = db.Column(db.String)
    user_email = db.Column(db.String)
    # user_profile_pic = db.Column()
    
    #create user  host one-to-one relationship
    host = db.relationship("Host", backref='user', lazy = True)
    
    #create one to many relationship user and order (one user has many orders)
    orders = db.relationship('Order', backref='user', lazy = True)
    
    def get_user_info(self):
        
        return{
            "User ID" : self.user_id,
            "Username": self.username,
            "Email": self.user_email,
            "Full name" : self.user_full_name,
            "Address" : self.user_address,
            "Phone number" : self.user_phone
        }
    