from app import db 
from datetime import datetime, timedelta

class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_of_order = db.Column(db.DateTime, nullable = False)
    #order_status = db.column()
    
    #create a relationship with experience and users
    
    
    def get_order_details(self):
        return {
            "Order ID" : self.order_id,
            "Date of order": self.date_of_order,
            #user_info
            #total cost
        
        }