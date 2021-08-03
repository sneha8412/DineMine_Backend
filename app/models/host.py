#-----------------------WAVE 2-----------------------------------------
from app import db 

class Host(db.Model):
    host_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    host_full_name = db.Column(db.String)
    host_address = db.Column(db.String)
    host_phone = db.Column(db.String)
    host_introduction = db.Column(db.String)
    # host_rating = db.Column(db.Integer) (this should be inside the user)
    # host_profile_pic = db.Column()
    
    #create one to many relationship between host and experience (one host can have many experiences posted)
    experiences = db.relationship('Experience', backref='host', lazy = True)
    
    #create one to one realtionship with the image 
    images = db.relationship('Image', backref='host', lazy = True)
    
    # user_profile_pic = db.Column()
    
    def get_host_info(self):
        
        return{
            "Host name": self.host_full_name,
            "Address" : self.host_address,
            "Phone number" : self.host_phone,
            "Introduction" :self.host_introduction,     
        }
        
    def get_host_info_id(self):
        
        return{
            "Host ID" : self.host_id,
            "Host name": self.host_full_name,
            "Address" : self.host_address,
            "Phone number" : self.host_phone,
            "Introduction" :self.host_introduction, 
            "Total Experiences" : len(self.experiences),
            "Experiences" : self.experiences #list of experiences
        }