from flask import Blueprint, json, request, jsonify, make_response
from app import db
# from app.models.board import Board
from .models.host import Host

host_bp = Blueprint("/", __name__, url_prefix="/")

#create a new host
@host_bp.route("", methods=["POST"], strict_slashes=False)
def create_a_host():
    request_body = request.get_json()
    if ("Host name" not in request_body or "Introduction" not in request_body or "Phone number" not in request_body or "Address" not in request_body):
        return jsonify({"details": "Failed to create a host profile"}), 400
    
    new_host = Host(hostname= request_body["Host name"],  introduction= request_body["Introduction"], address= request_body["Address"], phonenum= request_body["Phone number"])
    db.session.add(new_host)
    db.session.commit()
    return jsonify({"Success": f"Host {new_host.hostname} is created"}), 201

#get a host profile
@host_bp.route("/<host_id>", methods=["GET"])
def get_a_host_profile(host_id):
    host = Host.query.get(host_id)
    if host== None:
        return jsonify({"Error": "Host is not found"}, 404)
    else:
        return make_response(host.get_host_info(), 200)
    
#get all the hosts in that location
@host_bp.route("", methods=["GET"])
def get_all_hosts_profiles():
    pass
    #filter by location date cuisine
    #sort by price and rating
    

#update a host profile


#delete a host profile
@host_bp.route("/<user_id>", methods=["DELETE"])
def delete_a_host_profile(host_id):
    host = Host.query.get(host_id)
    db.session.delete(host)
    db.session.commit() #how can we transfer this to a seperate column of deleted hosts
    return jsonify({"Success": "Host is deleted"}, 200)

#deactivate the host temporarily

