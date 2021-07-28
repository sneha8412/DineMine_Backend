from app import db 
from datetime import datetime

class Experience(db.Model):
    exp_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exp_title = db.Column(db.String(50))
    #cuisine list
    exp_price = db.Column(db.Decimal(6,2))
    exp_description = db.Column(db.String(500))
    #dine time
    #pictures
    
    #order_status = db.column()
    
    #create a relationship with host 
    
    
    def get_exp(self):
        return {
            "Experience ID" : self.exp_id,
            "Title" : self.exp_title,
            "Price" : self.exp_price,
            "Description" : self.exp_description
            #host id
            #order id
            
        }