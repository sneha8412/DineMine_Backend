from flask import Blueprint, json, request, jsonify, make_response, Response
from app import db, helper
from .models.image import Image
from .models.host import Host
from flask import Flask, request, Response
from werkzeug.utils import secure_filename


image_bp = Blueprint("/images", __name__, url_prefix="/images")

@image_bp.route('/host/<host_id>/upload', methods=['POST'])
def upload(host_id):
    
    print("request = " + str(request.files));
    pic = request.files['pic']
    if not pic:
        return 'No pic uploaded!', 400

    if (not helper.is_int(host_id)):
        return 'Invalid host id!', 400

    host = Host.query.get(host_id)

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    if not filename or not mimetype:
        return 'Bad upload!', 400

    img = Image(img=pic.read(), name=filename, mimetype=mimetype)
    
    host.images.append(img)
    
    db.session.add(img)
    db.session.add(host)
    
    db.session.commit()

    return jsonify({ "img_id": img.id, "details": f"img uploaded for host {host.host_id}"}), 200


@image_bp.route('<image_id>',methods=['GET'])
def get_img(image_id):
    print(f"image id: {image_id}")
    img = Image.query.filter_by(id=image_id).first()
    if not img:
        return 'Img Not Found!', 404

    return Response(img.img, mimetype=img.mimetype)