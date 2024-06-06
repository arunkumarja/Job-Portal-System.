from celery import shared_task

@shared_task(bind=True)
def test_func(self):
    #operations
    for i in range(8):
        print(i)
    return "Done"

@shared_task()
def Job_send_mail():
    a=[]
    employee =Job_Seekers.objects.all()
    for emp in employee:
        x=emp.skills['skill']
    job_details = JobDetails.objects.all()
    for detail in job_details:
        y=detail.key_skills['Skills']
    for i in x:
        if i in y:
            a.append(i)
    return a        


    return "MSG DONE"

    