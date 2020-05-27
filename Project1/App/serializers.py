from rest_framework import serializers
from App.models import *






class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','nickname']
