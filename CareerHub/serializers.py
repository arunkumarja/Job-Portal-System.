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


class Job_SeekersSerializer1(serializers.ModelSerializer):
    class Meta:
        model=Job_Seekers       
        fields=['name','email','skills','location']       

class JobDetailsserializer(serializers.ModelSerializer):
    class Meta:
        model=JobDetails
        fields='__all__'

        
               
class JobApplicationserializer(serializers.ModelSerializer):
     
    job_opening=JobDetailsserializer()
    Job_Seekers=Job_SeekersSerializer()
    class Meta:
        model=JobApplication
        fields='__all__'               

         