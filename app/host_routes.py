
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
    if ("name" not in request_body):
        return jsonify({"details": "Host name required to create a host"}), 400
    
    new_host = Host.from_json(request_body)
    
    db.session.add(new_host)
    db.session.commit()
    return jsonify({ "host_id":new_host.host_id, "Success": f"Host {new_host.host_full_name} is created"}), 201


#get a host profile
@host_bp.route("/<host_id>", methods=["GET"])
def get_a_host_profile(host_id):
    host = Host.query.get(host_id)
    if host== None:
        return jsonify({"Error": "Host is not found"}, 404)
    else:
        return make_response(host.get_host_info(), 200)
    
    
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
        updated_host = Host.from_json(form_data)
        
        host.update_host(updated_host)
        
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

# #get all experiences for the host
# @host_bp.route("/<host_id>/experiences", methods=["GET"])
# def get_all_experiences_for_host_profile(host_id):
#     host = Host.query.get(host_id)
#     if host== None:
#         return jsonify({"Error": "Host is not found"}, 404)
#     else:
#         return make_response(host.experiences, 200)

#get one experience for the host
@host_bp.route("/<host_id>/experiences/<experience_id>", methods=["GET"])
def get_all_experiences_for_host_profile(host_id, experience_id):
    pass


#----------------STRETCH GOAL------------------------------------------
#deactivate the host temporarily

