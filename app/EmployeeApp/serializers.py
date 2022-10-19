from rest_framework import serializers
from .models import Employee, Work_Arrangement

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model =Employee
        fields = '__all__'
        

class Work_ArrangementSerializer(serializers.ModelSerializer):
    class Meta:
        model =Work_Arrangement
        fields = '__all__'