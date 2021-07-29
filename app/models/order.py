
#------------------WAVE 4--------------------------------------
from app import db 
from datetime import datetime, timedelta

class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_of_order = db.Column(db.DateTime, nullable = False)
    #order_status = db.column()
    
    #create a relationship users (one user has many orders)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    
    #create a relationship Experience (one experience has many orders)
    exp_id = db.Column(db.Integer, db.ForeignKey('experience.exp_id'))
    
    
    def get_order_details(self):
        return {
            "Order ID" : self.order_id,
            "Date of order": self.date_of_order,
            "Experience ID" : self.exp_id,
            "User ID" : self.user_id
            #total cost
        
        }