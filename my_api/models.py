from django.db import models

# Create your models here.
class Data(models.Model) :
    slack_name = models.CharField(max_length=250)
    current_day = models.CharField(max_length=10)
    utc_time = models.DateTimeField()
    track = models.CharField(max_length=250)
    github_file_url = models.URLField()
    github_repo_url = models.URLField()
