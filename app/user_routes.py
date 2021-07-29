from flask import Blueprint, json, request, jsonify, make_response
from app import db
# from app.models.board import Board
from .models.user import User

user_bp = Blueprint("/users", __name__, url_prefix="/")

#create a new user
@user_bp.route("", methods=["POST"], strict_slashes=False)
def create_a_user():
    request_body = request.get_json()
    if ("Username" not in request_body or "Full name" not in request_body or "Phone number" not in request_body or "Address" not in request_body):
        return jsonify({"details": "Failed to create a user profile"}), 400
    
    new_user = User(username= request_body["Username"], fullname = request_body["Full name"], address= request_body["Address"], phonenum= request_body["Phone number"])
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
    
#update a user profile


#delete a user profile
@user_bp.route("/<user_id>", methods=["DELETE"])
def delete_a_user_profile(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit() #how can we transfer this to a seperate column of deleted users
    return jsonify({"Success": "User is deleted"}, 200)

