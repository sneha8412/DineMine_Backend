#----------------------------WAVE 1 -----------------------------------------------

from flask import Blueprint, json, request, jsonify, make_response, Response
from app import db
from .models.user import User

user_bp = Blueprint("/users", __name__, url_prefix="/users")


#create a new user
@user_bp.route("", methods=["POST"], strict_slashes=False)
def create_a_user():
    request_body = request.get_json()
    if ("Full name" not in request_body or "Email" not in request_body):
        return jsonify({"details": "Failed to create a user profile"}), 400
    
    address = ""
    if ("Address" in request_body):
        address =  request_body["Address"];
    
    phone = ""
    if ("Phone number" in request_body):
        phone =  request_body["Phone number"];     
    
    new_user = User(username= request_body["Username"],
                    user_full_name = request_body["Full name"], 
                    user_address = address, 
                    user_phone = phone,
                    user_email = request_body["Email"])
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({ "user_id": new_user.user_id, "Success": f"User {new_user.username} is created"}), 201


#get a user profile
@user_bp.route("/<user_id>", methods=["GET"])
def get_a_user_profile(user_id):
    user = User.query.get(user_id)
    if user == None:
        return jsonify({"Error": "User is not found"}, 404)
    else:
        return make_response(user.get_user_info(), 200)


#get all users
@user_bp.route("", methods=["GET"])
def get_all_users():
    
    user_email_filter = request.args.get("email")
    
    matching_users = []
    if (user_email_filter is not None):
        matching_users = User.query.filter_by(user_email = user_email_filter)
    else:
        matching_users = User.query.all()
    
    user_response = []
    for user in matching_users:
        user_response.append(user.get_user_info())
    return jsonify(user_response), 200


#delete a user profile
@user_bp.route("/<user_id>", methods=["DELETE"])
def delete_a_user_profile(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit() #how can we transfer this to a seperate column of deleted users
    return jsonify({"Success": "User is deleted"}, 200)

#-----------------------STRETCH GOALS------------------------------------------
    
#update a user profile empty for now
@user_bp.route("/<user_id>", methods=["PUT"])
def update_a_user_profile(user_id):   
      
    user  = User.query.get(user_id)
    
    if user == None or not user:
        return Response("User not found", 404)
    
    form_data = request.get_json()
    
    if (form_data != None):
        if ("Username" in form_data.keys()):
            user.username = form_data["Username"]
        
        if ("Full name" in form_data.keys()):
             user.user_full_name = form_data["Full name"]
            
        if ("Address" in form_data.keys()):
             user.user_address = form_data["Address"]
        
        if ("Phone number" in form_data.keys()):
            user.user_phone = form_data["Phone number"]
        
        db.session.add(user)
        db.session.commit()
        
        return user.get_user_info(), 200
    
    return jsonify({"details": "Failed to update user, please try again"}), 400