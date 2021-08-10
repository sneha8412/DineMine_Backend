
#----------------------WAVE 3 -------------------------------------------

from app import db 
from datetime import datetime

class Experience(db.Model):
    exp_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exp_title = db.Column(db.String(50))
    cuisine = db.Column(db.String(20))
    exp_price = db.Column(db.Float)
    exp_description = db.Column(db.String(500))
    dinetime = db.Column(db.String(15))
    city = db.Column(db.String)
    #pictures
    #order_status = db.column()
    
    #create a relationship with host (one host can have many experiences)
    host_id = db.Column(db.Integer, db.ForeignKey('host.host_id'))
    
    #create a relationship with order - one experience can have many orders
    orders =  db.relationship('Order', backref='experience', lazy = True)
    
    #create a realtionship with images - one experience can have many images
    images =  db.relationship('Image', backref='experience', lazy = True)
    
    def get_exp_info(self):
        return {
            "Experience ID" : self.exp_id,
            "Host ID" : self.host_id,
            "Title" : self.exp_title,
            "Price" : self.exp_price,
            "Description" : self.exp_description,
            "Cuisine" :self.cuisine,
            "Dine time" : self.dinetime,
            "City": self.city
            
        }
        
    def get_exp_order_info(self):
        return{
            # "Orders":self.orders,
            "Experience ID" : self.exp_id,
            "Host ID" : self.host_id,
            "Title" : self.exp_title,
            "Price" : self.exp_price,
            "Description" : self.exp_description,
            "Cuisine" :self.cuisine,
            "Dine time" : self.dinetime,
            "City" : self.city
        }