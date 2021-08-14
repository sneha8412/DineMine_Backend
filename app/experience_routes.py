#--------------------------WAVE 3 ------------------------------------
from flask import Blueprint, json, request, jsonify, make_response, Response
from app import db
# from app.models.board import Board
from .models.host import Host
from .models.experience import Experience
from .models.image import Image
from sqlalchemy import desc, asc

experience_bp = Blueprint("/experiences", __name__, url_prefix="/experiences")

#create a new experience
@experience_bp.route("/hosts/<host_id>", methods=["POST"], strict_slashes=False)
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
        "Dine time" not in request_body or
        "City" not in request_body or
        "Total number of guests" not in request_body):
        
        return jsonify({"details": "Failed to create experience"}), 400
    
    new_experience = Experience( 
                    exp_description=request_body["Description"],
                    exp_title=request_body["Title"], 
                    cuisine=request_body["Cuisine"], 
                    exp_price =request_body["Price"],
                    dinetime=request_body["Dine time"],
                    city=request_body["City"],
                    total_number_of_guests= request_body["Total number of guests"]
                    )
    
    host.experiences.append(new_experience)
    
    db.session.add(new_experience)
    db.session.add(host)
    db.session.commit()
    return jsonify({ "experience_id": new_experience.exp_id, "Success": f"Experience {new_experience.exp_title} is created"}), 201

#----------------------------------------------------------------------------------------------------------------------------
#get experience by location
@experience_bp.route("", methods=["GET"], strict_slashes=False)
def get_all_experiences():
    
     
    sort_by_price = request.args.get("sort")
    location_query = request.args.get("city")
    dinetime_query = request.args.get("dinetime")
    cuisine_query = request.args.get("cuisine")
    
    exp_list = []
    
    # experiences = Experience.query.all()
    
    #filter by location  
    if location_query is not None:
        # print("location query")
        experiences = Experience.query.filter_by(city = location_query)
    # filter by dinetimes
    elif dinetime_query is not None:
        # print("dinetime query " + str(dinetime_query)) 
        experiences = Experience.query.filter_by(dinetime = dinetime_query)
    # filter by cuisine type
    elif cuisine_query is not None:
        # print("cuisine query" + str(cuisine_query) )
        experiences = Experience.query.filter_by(cuisine = cuisine_query)
    else:
        experiences = Experience.query.all()

    #sort by price
    if sort_by_price is not None:
        if sort_by_price == "asc":
            experiences = db.session.query(Experience).order_by(asc(Experience.exp_price))
        else:    
            experiences = db.session.query(Experience).order_by(desc(Experience.exp_price))
        
    for exp in experiences:
        
        expImages = db.session.query(Image).filter(Image.exp_id == exp.exp_id).all()
        
        expFirstImageId = ""
        if (expImages != None and len(expImages) > 0):
            expFirstImageId = expImages[0].id   
        
        exp_list.append(exp.get_exp_info_with_image(expFirstImageId))        
    
    return jsonify(exp_list), 200

#------------------------------------------------------------------------------------------------------
#get an experience
@experience_bp.route("<experience_id>", methods=["GET"], strict_slashes=False)
def get_an_experience_detail(experience_id):
    experience = Experience.query.get(experience_id)
    if experience == None:
        return jsonify({"Error": "Experience not found"}, 404)
    else:
        return make_response(experience.get_exp_info(), 200)

#------------------------------------------------------------------------------------------------------
# #get all experience based of one host
@experience_bp.route("/hosts/<host_id>", methods=["GET"], strict_slashes=False)
def get_host_experiences(host_id):
    
    host = Host.query.get(host_id)
    
    exp_response = []
    for experience in host.experiences:
        exp_response.append(experience.get_exp_info())
    return jsonify(exp_response), 200


#--------------------------------------------------------------------------------------------------------
#update an experience (host does this)
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
        
        if ("City" in form_data.keys()):
            experience.city = form_data["City"]
            
        if ("Total number of guests" in form_data.keys()):
            experience.total_number_of_guests = form_data["Total number of guests"]
            
        
        db.session.add(experience)
        db.session.commit()
        
        return experience.get_exp_info(), 200
    
    return jsonify({"details": "Failed to update, please try again"}), 400

#----------------------------------------------------------------------------------------------------
#delete an Experience
@experience_bp.route("/<experience_id>", methods=["DELETE"])
def delete_an_experience(experience_id):
    
    experience = Experience.query.get(experience_id)
    
    if experience == None:
        return jsonify({"details" : f"No experience with ID number {experience_id} found "},404)
    
    db.session.delete(experience)
    db.session.commit() #how can we transfer this to a seperate column of deleted hosts
    
    return jsonify({"Success": "Experience is deleted"}), 200

#----------------------------------------------------------------------------------------------------
# #delete all Experiences
# @experience_bp.route("/hosts/<host_id>", methods=["DELETE"])
# def delete_all_experiences_for_a_host(host_id):
    
#     host = Host.query.get(host_id)
    
#     if not host or host == None:
#         return jsonify({"details": "No Host found"}), 404
    
#     # experiences = Experience.query.get(host_id)
    
#     # if len(host.experiences) == 0:
#     #    return jsonify({"details" : f"No experiences found "},404)
    
#     db.session.delete(host.experiences)
#     db.session.commit()
        
#     return jsonify({"Success": "All Experiences for host is deleted"}), 200
 