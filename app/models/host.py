from app import db 

class Host(db.Model):
    host_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    host_full_name = db.Column(db.String)
    host_address = db.Column(db.string)
    host_phone = db.Column(db.string)
    host_introduction = db.Column(db.string(200))
    host_rating = db.Column(db.integer(5))
    # host_profile_pic = db.Column()
    
    #create one to many relationship between host and experience
    
    # user_profile_pic = db.Column()
    
    def get_host_info(self):
        
        return{
            "Host name": self.host_full_name,
            "Address" : self.host_address,
            "Phone number" : self.host_phone,
            "Introduction" :self.host_introduction,     
        }