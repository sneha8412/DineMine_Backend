#----------------------------WAVE 1 -----------------------------------------------

from flask import Blueprint, json, request, jsonify, make_response
from app import db
from .models.user import User

user_bp = Blueprint("/users", __name__, url_prefix="/users")


#create a new user
@user_bp.route("", methods=["POST"], strict_slashes=False)
def create_a_user():
    request_body = request.get_json()
    if ("Username" not in request_body or "Full name" not in request_body or "Phone number" not in request_body or "Address" not in request_body):
        return jsonify({"details": "Failed to create a user profile"}), 400
    
    new_user = User(username= request_body["Username"],
                    user_full_name = request_body["Full name"], 
                    user_address=request_body["Address"], 
                    user_phone=request_body["Phone number"])
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"Success": f"User {new_user.username} is created"}), 201


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
    users = User.query.all()
    
    user_response = []
    for user in users:
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