import datetime
import jwt
from django.conf import settings
from uuid import uuid4

def Generate_Access_Token(user):
    access_token_payload = {
        'token_type':'access',
        'id':user.id,
        #'user_name':user.username,
        'exp':datetime.datetime.utcnow()+datetime.timedelta(days=0,minutes=5),
        'iat':datetime.datetime.utcnow(),
        'jti': uuid4().hex
    }

    access_token = jwt.encode(access_token_payload,settings.SECRET_KEY,algorithm='HS256').decode('utf-8')
    return access_token


def Generate_Refresh_Token(user):
    refresh_token_payload = {
        'token_type':'refresh',
        'id': user.id,
        'exp' :datetime.datetime.utcnow()+datetime.timedelta(days=7),
        'iat':datetime.datetime.utcnow(),
        'jti': uuid4().hex
    }

    refresh_token = jwt.encode(refresh_token_payload,settings.SECRET_KEY,algorithm='HS256').decode('utf-8')
    return refresh_token
