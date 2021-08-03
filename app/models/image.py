from app import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.LargeBinary, unique=False, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    
    #create relationship with host (one host has one image)
    host_id = db.Column(db.Integer, db.ForeignKey('host.host_id'))
    
    #create relationship with experience (one experience can have many photos -ideally minimum 5 photos)
    exp_id = db.Column(db.Integer, db.ForeignKey('experience.exp_id'))