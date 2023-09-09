from django.shortcuts import render
from django.http import JsonResponse
from .models import Data
import datetime


# Create your views here.
def get_data(request) :
    slack_name = request.GET.get('slack_name', 'Abdulhaleem_Sanuth')
    track = request.GET.get('track', 'backend')
    
    current_day = datetime.datetime.utcnow().strftime('%A')
    current_time = datetime.datetime.utcnow()

    github_file_url = 'https://github.com/Abdulhaleem-6/endpoint/blob/main/my_api/views.py'
    github_repo_url = 'https://github.com/Abdulhaleem-6/endpoint'

    info = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    Data.objects.create(**info)

    return JsonResponse(info)



