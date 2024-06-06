from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import *
from django.http import HttpResponse

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
import json

class JobDetailsAPI(APIView):
    def get(self,request):
        role_id = request.query_params.get('role_id')
        try:
            job_opening_instance = JobDetails.objects.get(id=role_id)
            job_applications = JobApplication.objects.filter(job_opening=job_opening_instance)
            job_application_count = job_applications.count()
            job_seekers = Job_Seekers.objects.filter(jobapplication__in=job_applications)
            job_seekers_serializer = Job_SeekersSerializer1(job_seekers, many=True)
            
            response_data = {
                "job_role": job_opening_instance.role,
                "job_application_count": job_application_count,
                "application_details": job_seekers_serializer.data
            }
            return Response(response_data)  
        except Exception as e:
            return Response(f'{e}')    

    def post(self,request):
        try:

            job=JobDetailsserializer(data=request.data)
            if job.is_valid():
                job.save()
                return Response("successfully created")
            return Response(job.errors)
        except Exception as e:
            return Response(f'{e}')           
    


class JobApplicationAPI(APIView):
    def post(self,request):
        job_seeker=request.POST.get('job_seeker')
        job_opening=request.POST.get('job_opening')
        Resume=request.FILES['resume']
        try:
            job_seeker_instance = Job_Seekers.objects.get(id=job_seeker)
            job_opening_instance = JobDetails.objects.get(id=job_opening)
            
            application = JobApplication(
                job_seeker=job_seeker_instance,
                job_opening=job_opening_instance,
                resume=Resume
            )
            application.save()
            return Response({
                "message": "Job applied successfully",
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(f"{e}")    


def test(request):
    test_func.delay()
    return HttpResponse("Done")


def Job_msg(request):
    Job_send_mail.delay()
    return HttpResponse("send")