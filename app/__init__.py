from flask import Flask
import os
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

# @app.route('/',methods=['GET', 'POST'])
#@cross_origin() #allow all origins all methods.
def create_app():
    app = Flask(__name__)
    #change to mysql
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    # Import models here for Alembic setup
    from app.models.user import User
    from app.models.host import Host
    from app.models.order import Order
    from app.models.experience import Experience
    from app.models.image import Image

    db.init_app(app)
    migrate.init_app(app, db)

    #import Blueprints here
    from .user_routes import user_bp
    from .host_routes import host_bp
    from .order_routes import order_bp
    from .experience_routes import experience_bp
    from .image_routes import image_bp
    
    #Register Blueprints here
    app.register_blueprint(user_bp)
    app.register_blueprint(host_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(experience_bp)
    app.register_blueprint(image_bp)
    
    #CORS(app)
    return app

#if __name__ == '__main__':
    #create_app.run()