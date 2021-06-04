from flask import Blueprint
from flask_apispec import doc, use_kwargs, marshal_with
from serializers.mypage import *
from service.mypage import *
from flask_jwt_extended import jwt_required, get_jwt


mypage = Blueprint("mypage", __name__, url_prefix="/mypage")

@doc(tags=['mypage'], description='해당 코디 정보들을 조회함.')
@mypage.route('/my-looks',methods=['GET'])
@jwt_required()
@marshal_with(MyLooksSchema(many=True))
def get_my_looks():
    uid=get_jwt()['sub']
    return MyPageService.my_looks(uid)