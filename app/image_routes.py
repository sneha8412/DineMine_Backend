from flask import Blueprint, json, request, jsonify, make_response, Response
from app import db
from .models.image import Image

from flask import Flask, request, Response
from werkzeug.utils import secure_filename


image_bp = Blueprint("/images", __name__, url_prefix="/images")

@image_bp.route('upload', methods=['POST'])
def upload():
    pic = request.files['pic']
    if not pic:
        return 'No pic uploaded!', 400

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    if not filename or not mimetype:
        return 'Bad upload!', 400

    img = Image(img=pic.read(), name=filename, mimetype=mimetype)
    db.session.add(img)
    db.session.commit()

    return 'Img Uploaded!', 200


@image_bp.route('<image_id>',methods=['GET'])
def get_img(image_id):
    print(f"image id: {image_id}")
    img = Image.query.filter_by(id=image_id).first()
    if not img:
        return 'Img Not Found!', 404

    return Response(img.img, mimetype=img.mimetype)