
from django.db import models


class Employer(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class JobDetails(models.Model):
    employer = models.ForeignKey('Employer', on_delete=models.CASCADE, related_name='job_openings')
    role = models.CharField(max_length=100)
    Company=models.CharField(max_length=200)
    experience = models.IntegerField(null=True)
    key_skills = models.JSONField()
    education = models.JSONField()
    employment_type = models.CharField(max_length=100)
    job_description = models.TextField()
    locations = models.JSONField(max_length=20)
    salary = models.CharField(max_length=10)
    profile_summary = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    applications_count = models.IntegerField(default=0)

    def __str__(self):
        return f"job role {self.role} and {self.experience}"

    def update_applications_count(self):
        self.applications_count = self.JobApplication_set.count()
        self.save()    

class Job_Seekers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    resume = models.FileField(upload_to='resumes/')
    skills = models.JSONField()
    experience = models.IntegerField(null=True)
    education = models.JSONField()
    expected_salary = models.CharField(null=True,max_length=10)
    notice_period = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"Jobseeker {self.name} "

class JobApplication(models.Model):
    job_seeker = models.ForeignKey('Job_Seekers', on_delete=models.CASCADE)
    job_opening = models.ForeignKey('JobDetails', on_delete=models.CASCADE)
    resume = models.FileField(upload_to='applications/')
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application for {self.job_opening.role} by {self.job_seeker.name}"
