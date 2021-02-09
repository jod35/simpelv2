from flask import Blueprint,jsonify,make_response

api_bp=Blueprint('api',__name__)

@api_bp.route('/')
def index():
    return make_response(
        {
            "message":"Hello"
        }
    )