# Generated by Django 4.2.13 on 2024-06-04 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CareerHub', '0002_jobdetails_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_seekers',
            name='contact',
        ),
    ]
