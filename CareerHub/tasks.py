from celery import shared_task

@shared_task(bind=True)
def test_func(self):
    #operations
    for i in range(8):
        print(i)
    return "Done"

def Job_send_mail(self):
    employee =Job_Seekers.objects.all()
    emp=employee.skills
    print(emp)
    job_details=JobDetails.objects.all()
    job=job_details.skills
    print(job)

    