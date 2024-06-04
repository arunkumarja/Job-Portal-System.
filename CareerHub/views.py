from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EmployeerAPI(APIView):
    def post(self,request):
        try:
            serializers=EmployersSerailzer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response({"message": "Successfully created"}, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(f'{e}')


class Job_seekerAPI(APIView):
    def post(self,request):
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        Password=request.POST.get('password')
        Resume=request.FILES['resume']
        Skills=request.POST.get('skills')
        Education=request.POST.get('education')
        Exprience=request.POST.get('experience')
        Expected_salary=request.POST.get('expected_salary')
        Notice_period=request.POST.get('notice_period')
        location=request.POST.get('location')

        try:
            job=Job_Seekers(name=Name,location=location,notice_period=Notice_period,expected_salary=Expected_salary,email=Email,password=Password,resume=Resume,skills=Skills,education=Education,experience=Exprience)
            job.save()
            return Response({"message": "Successfully created"}, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response(f'{e}')        


class JobDetailsAPI(APIView):
    def post(self,request):
        try:
            jobdetails=JobDetailsserializer(data=request.data)
            if jobdetails.is_valid():
                jobdetails.save()
                return Response("successfully cretated")
            return Response(jobdetails.errors)  
        except Exception as e:
            return Response(f'{e}')      
    


class JobApplicationAPI(APIView):
    def post(self,request):
        job_seeker=request.POST.get('job_seeker')
        print(job_seeker)
        job_opening=request.POST.get('job_opening')
        Resume=request.FILES['resume']
        try:
            job_seeker_instance = Job_Seekers.objects.get(id=job_seeker)
            job_opening_instance = JobDetails.objects.get(id=job_opening)
            print(job_seeker_instance)
            print(job_opening_instance)
            application = JobApplication(job_seeker=job_seeker_instance, job_opening=job_opening_instance, resume=Resume)
            application.save()
            return Response("job applied success")
        except Exception as e:
            return Response(f"{e}")    
