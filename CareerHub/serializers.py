from .models import *
from rest_framework import serializers

class EmployersSerailzer(serializers.ModelSerializer):
    class Meta:
        model=Employer
        fields='__all__'


class Job_SeekersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job_Seekers       
        fields='__all__'

class JobDetailsserializer(serializers.ModelSerializer):
    class Meta:
        model=JobDetails
        fields='__all__'       

         