from flask import Blueprint, json, request, jsonify, make_response, Response
from app import db, helper
from .models.image import Image
from .models.host import Host
from .models.experience import Experience
from flask import Flask, request, Response
from werkzeug.utils import secure_filename


image_bp = Blueprint("/images", __name__, url_prefix="/images")

@image_bp.route('/host/<host_id>/upload', methods=['POST'])
def upload_host_image(host_id):
    
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
    
    host.images.clear()
    host.images.append(img)
    
    db.session.add(img)
    db.session.add(host)
    
    db.session.commit()

    return jsonify({ "img_id": img.id, "details": f"img uploaded for host {host.host_id}"}), 201

# Add an image for an experience
@image_bp.route('/experience/<exp_id>/upload', methods=['POST'])
def upload_experience_image(exp_id):
    
    print("request = " + str(request.files));
    pic = request.files['pic']
    if not pic:
        return 'No pic uploaded!', 400

    if (not helper.is_int(exp_id)):
        return 'Invalid exp id!', 400

    exp = Experience.query.get(exp_id)

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    if not filename or not mimetype:
        return 'Bad upload!', 400

    img = Image(img=pic.read(), name=filename, mimetype=mimetype)
    
    exp.images.append(img)
    
    db.session.add(img)
    db.session.add(exp)
    
    db.session.commit()

    return jsonify({ "img_id": img.id, "details": f"img uploaded for experience {exp.exp_id}"}), 201


@image_bp.route('<image_id>',methods=['GET'])
def get_img(image_id):
    print(f"image id: {image_id}")
    img = Image.query.filter_by(id=image_id).first()
    if not img:
        return 'Img Not Found!', 404

    return Response(img.img, mimetype=img.mimetype)

# Downloads the host image
@image_bp.route('/host/<host_id>', methods=['GET'])
def get_host_image(host_id):

    host = Host.query.get(host_id)
    
    if (len(host.images) > 0):
        image = host.images[0]
        
        return Response(image.img, mimetype=image.mimetype)
    
    return 'Host has no image!', 404

# Gets all the images associated with an experience
@image_bp.route('/experience/<exp_id>', methods=['GET'])
def get_experience_images(exp_id):

    exp = Experience.query.get(exp_id)
    
    if (not exp):
        f'No experience found for id = {exp_id}!', 404
    
    exp_images = []
    
    if (len(exp.images) > 0):
        for exp_img in exp.images:
          exp_images.append(exp_img.to_json())
        
        #return Response(exp_images), 200  
        
    return jsonify(exp_images), 200