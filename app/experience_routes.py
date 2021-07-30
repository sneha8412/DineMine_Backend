#--------------------------WAVE 3 ------------------------------------
from flask import Blueprint, json, request, jsonify, make_response, Response
from app import db
# from app.models.board import Board
from .models.host import Host
from .models.order import Order
from .models.experience import Experience

experience_bp = Blueprint("/hosts/<host_id>/", __name__, url_prefix="/hosts/<host_id>/")

#create a new experience
@experience_bp.route("", methods=["POST"], strict_slashes=False)
def create_an_experience(host_id):
    
    host = Host.query.get(host_id)
    #print(f"##### {board_id} #####")
    
    if not host or host == None:
        return jsonify({"details": "No Host found"}), 404
    
    request_body = request.get_json()
    if ("Title" not in request_body or 
        "Price" not in request_body or 
        "Description" not in request_body or
        "Cuisine" not in request_body or 
        "Dine time" not in request_body 
        ):
        return jsonify({"details": "Failed to create experience"}), 400
    
    new_experience = Experience( 
                    exp_description=request_body["Description"],
                    exp_title=request_body["Title"], 
                    cuisine=request_body["Cuisine"], 
                    exp_price =request_body["Price"],
                    dinetime=request_body["Dine time"]
                    )
    
    db.session.add(new_experience)
    db.session.add(host)
    db.session.commit()
    return jsonify({"Success": f"Experience {new_experience.exp_title} is created"}), 201


#get an experience
@experience_bp.route("<experience_id>", methods=["GET"], strict_slashes=False)
def get_an_experience_detail(experience_id):
    experience = Experience.query.get(experience_id)
    if experience == None:
        return jsonify({"Error": "Experience not found"}, 404)
    else:
        return make_response(experience.get_exp_info(), 200)


# #get all experience based of one host
# @experience_bp.route("", methods=["GET"], strict_slashes=False)
# def get_an_experience_detail():
#     experiences = Experience.query.all()
    
#     exp_response = []
#     for experience in experiences:
#         exp_response.append(experience.get_exp_info())
#     return jsonify(exp_response), 200

#get all experience based on one location


    
#update the experience (host does this)
@experience_bp.route("<experience_id>", methods=["PUT"], strict_slashes=False)
def update_an_experience_detail(experience_id):     
    experience  = Experience.query.get(experience_id)
    
    if experience == None or not experience:
        return Response("Host not found", 404)
    
    form_data = request.get_json()
    
    if (form_data != None):
        if ("Title" in form_data.keys()):
            experience.exp_title = form_data["Title"]
        
        if ("Price" in form_data.keys()):
             experience.exp_price = form_data["Price"]
            
        if ("Description" in form_data.keys()):
             experience.exp_description = form_data["Description"]
        
        if ("Cuisine" in form_data.keys()):
            experience.exp_description = form_data["Cuisine"]
        
        if ("Dine time" in form_data.keys()):
            experience.dinetime = form_data["Dine time"]
            
        
        db.session.add(experience)
        db.session.commit()
        
        return experience.get_experience_info(), 200
    
    return jsonify({"details": "Failed to update, please try again"}), 400