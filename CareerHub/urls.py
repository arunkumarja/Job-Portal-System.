"""
URL configuration for Core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from .views import *

urlpatterns = [
   
   path('employee/',EmployeerAPI.as_view(),name='employee'),
   path('job_seeker/',Job_seekerAPI.as_view(),name='job_seeker'),
   path('job_details/',JobDetailsAPI.as_view(),name='job_details'),
   path('job_apply/',JobApplicationAPI.as_view(),name='job_apply'),
   path('test/',test,name='send'),
   path('job/',Job_msg,name='job')

]
