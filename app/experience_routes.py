from flask import Blueprint, json, request, jsonify, make_response
from app import db
# from app.models.board import Board
from .models.host import Host
from .models.order import Order
from .models.experience import Experience

experience_bp = Blueprint("/", __name__, url_prefix="/")

#create a new experience
@experience_bp.route("<experience_id>", methods=["POST"], strict_slashes=False)
def create_an_order(experience_id):
    pass

#get an experience
@experience_bp.route("<experience_id>", methods=["GET"], strict_slashes=False)
def get_an_experience_detail(experience_id):
    experience = Experience.query.get(experience_id)
    if experience == None:
        return jsonify({"Error": "Experience not found"}, 404)
    else:
        return make_response(experience.get_order_details(), 200)


#get all experience for one host



#get all experience in one location


    
#update the experience (host does this)
@experience_bp.route("<host_id>/<experience_id>", methods=["PUT"], strict_slashes=False)
def update_an_order_detail(experience_id):     
    pass