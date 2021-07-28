from app import db 

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.VARCHAR(20), unique=True)
    user_full_name = db.Column(db.String)
    user_address = db.Column(db.string)
    user_phone = db.Column(db.string)
    # user_profile_pic = db.Column()
    
    #create one to many relationship user and order
    
    def get_user_info(self):
        
        return{
            "Username": self.username,
            "Full name" : self.user_full_name,
            "Address" : self.user_address,
            "Phone number" : self.user_phone
        }
    