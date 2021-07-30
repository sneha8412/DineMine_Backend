
#---------------------------WAVE 2---------------------------------------------
from flask import Blueprint, json, request, jsonify, make_response, Response
from app import db
from app.models.experience import Experience
from .models.host import Host

host_bp = Blueprint("/hosts", __name__, url_prefix="/hosts")

#create a new host
@host_bp.route("", methods=["POST"], strict_slashes=False)
def create_a_host():
    request_body = request.get_json()
    if ("Host name" not in request_body or "Introduction" not in request_body or "Phone number" not in request_body or "Address" not in request_body):
        return jsonify({"details": "Failed to create a host profile"}), 400
    
    new_host = Host(host_full_name=request_body["Host name"], 
                    host_introduction=request_body["Introduction"], 
                    host_address=request_body["Address"], 
                    host_phone =request_body["Phone number"])
    
    db.session.add(new_host)
    db.session.commit()
    return jsonify({"Success": f"Host {new_host.host_full_name} is created"}), 201


#get a host profile
@host_bp.route("/<host_id>", methods=["GET"])
def get_a_host_profile(host_id):
    host = Host.query.get(host_id)
    if host== None:
        return jsonify({"Error": "Host is not found"}, 404)
    else:
        return make_response(host.get_host_info_id(), 200)
    
    
#get all the hosts in that location #filter by location
@host_bp.route("", methods=["GET"])
def get_all_hosts_profiles():
    
    hosts = Host.query.all()
    
    host_response = []
    for host in hosts:
        host_response.append(host.get_host_info_id())
    return jsonify(host_response), 200
    

#update a host profile
@host_bp.route("<host_id>", methods=["PUT"])
def update_a_host_profiles(host_id):
    
    host = Host.query.get(host_id)
    
    if host == None or not host:
        return Response("Host not found", 404)
    
    form_data = request.get_json()
    
    if (form_data != None):
        if ("Host name" in form_data.keys()):
            host.host_full_name = form_data["Host name"]
        
        if ("Address" in form_data.keys()):
            host.host_address = form_data["Address"]
            
        if ("Phone number" in form_data.keys()):
            host.host_phone = form_data["Phone number"]
        
        if ("Introduction" in form_data.keys()):
            host.host_introduction = form_data["Introduction"]
        
        db.session.add(host)
        db.session.commit()
        
        return host.get_host_info(), 200
    
    return jsonify({"details": "Failed to update, please try again"}), 400


#delete a host profile
@host_bp.route("/<host_id>", methods=["DELETE"])
def delete_a_host_profile(host_id):
    
    host = Host.query.get(host_id)
    
    if host == None:
        return jsonify({"details" : f"No host with ID number {host_id} found "},404)
    
    db.session.delete(host)
    db.session.commit() #how can we transfer this to a seperate column of deleted hosts
    
    return jsonify({"Success": "Host is deleted"}), 200

#--------------------WAVE 3-------------------------------------------

#get all experiences for the host
@host_bp.route("/<host_id>/experiences", methods=["GET"])
def get_all_experiences_for_host_profile(host_id):
    host = Host.query.get(host_id)
    if host== None:
        return jsonify({"Error": "Host is not found"}, 404)
    else:
        return make_response(host.experiences, 200)

#get one experience for the host


#----------------STRETCH GOAL------------------------------------------
#deactivate the host temporarily

