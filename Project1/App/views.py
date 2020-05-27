from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login
from rest_framework.decorators import api_view
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from App.models import *
#from App.serializers import *
from App.utils import Generate_Access_Token,Generate_Refresh_Token
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import get_user_model
import jwt
from django.conf import settings


@ensure_csrf_cookie
@api_view(['POST','GET',])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    response = Response()

    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        user = CustomUser.objects.filter(username=username).first()
        #serialized_user_data = UserSerial(user)
        access_token = Generate_Access_Token(user)
        refresh_token = Generate_Refresh_Token(user)
        response.data={'access_token':access_token,'refresh_token':refresh_token}
        return response
    else:
        return HttpResponse("USERNAME or PASSWORD ERROR!!!")
