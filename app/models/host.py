#-----------------------WAVE 2-----------------------------------------
from app import db 

class Host(db.Model):
    host_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    host_full_name = db.Column(db.String)
    host_address = db.Column(db.String)
    host_phone = db.Column(db.String)
    host_introduction = db.Column(db.String)
    host_email = db.Column(db.String)
    host_city = db.Column(db.String)
    #host_certified = db.Column(db.Boolean)
    # host_rating = db.Column(db.Integer) (this should be inside the user)
    # host_profile_pic = db.Column()
    
    #create one to many relationship between host and experience (one host can have many experiences posted)
    experiences = db.relationship('Experience', backref='host', lazy = True)
    
    #create one to one realtionship with the image 
    images = db.relationship('Image', backref='host', lazy = True)
    
    #create one-to-one with User
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    
    # user_profile_pic = db.Column()
    @staticmethod
    def from_json(host_json):
        host = Host()
        if ("name" in host_json):
            host.host_full_name=host_json["name"] 
        
        if ("intro" in host_json):
            host.host_introduction = host_json["intro"] 
        
        if ("address" in host_json):
            host.host_address=host_json["address"]
        
        if ("phone" in host_json):
            host.host_phone =host_json["phone"]
        
        if ("city" in host_json):
            host.host_city = host_json["city"]
            
        if ("email" in host_json):
            host.host_email = host_json["email"] 
        
        return host
    
    def update_host(self, updated_host):
        
        if (updated_host.host_full_name):
            self.host_full_name = updated_host.host_full_name
            
        if (updated_host.host_address):
            self.host_address = updated_host.host_address
        
        if (updated_host.host_phone):
            self.host_phone = updated_host.host_phone
            
        if (updated_host.host_email):
            self.host_email = updated_host.host_email

        if (updated_host.host_city):
            self.host_city = updated_host.host_city
            
        if (updated_host.host_introduction):
            self.host_introduction = updated_host.host_introduction

    
    def get_host_info(self):
        
        return{
            "id": self.host_id,
            "name": self.host_full_name,
            "address" : self.host_address,
            "phone" : self.host_phone,
            "intro" :self.host_introduction,
            "city" : self.host_city,
            "email" :self.host_email
                
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