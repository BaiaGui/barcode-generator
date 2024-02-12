from flask import Blueprint, request, jsonify

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.post('/create_tag')
def create_tags():
    print(request.json)
    return jsonify({"res":"ok"}), 200
