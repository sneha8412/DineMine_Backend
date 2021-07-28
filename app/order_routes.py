from flask import Blueprint, json, request, jsonify, make_response
from app import db
# from app.models.board import Board
from .models.user import User
from .models.order import Order
from .models.experience import Experience

order_bp = Blueprint("/", __name__, url_prefix="/")

#create a new order
@order_bp.route("<experience_id>", methods=["POST"], strict_slashes=False)
def create_an_order(experience_id):
    pass

#get an order detail
@order_bp.route("<order_id>", methods=["GET"], strict_slashes=False)
def get_an_order_detail(order_id):
    order = Order.query.get(order_id)
    if order == None:
        return jsonify({"Error": "Order not found"}, 404)
    else:
        return make_response(order.get_order_details(), 200)
    
    
#update the status of the order (cancel)
@order_bp.route("<order_id>", methods=["PUT"], strict_slashes=False)
def update_an_order_detail(order_id):     
    pass
