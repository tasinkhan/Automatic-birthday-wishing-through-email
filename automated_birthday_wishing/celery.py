import os

from celery import Celery
from celery.schedules import crontab
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'automated_birthday_wishing.settings')

app = Celery('automated_birthday_wishing')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


# Manual periodic task scheduling
# app.conf.beat_schedule = {
#     #Scheduler Name
#     'send_birthday_wish_mail': {
#         # Task Name (Name Specified in Decorator)
#         'task': 'send_birthday_wish_mail',  
#         # Schedule      
#         'schedule': crontab(),
#     },
# }  

