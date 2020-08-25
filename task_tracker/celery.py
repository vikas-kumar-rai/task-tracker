from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_tracker.settings')

app = Celery('task_tracker')

app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.conf.beat_schedule = {
    'daily_update': {
        'task': 'task.tasks.daily_update',
        'schedule': crontab(minute=0, hour='17'),
        'args': ('daily_update@gmail.com',)
    },
    'weekly_update': {
        'task': 'task.tasks.weekly_update',
        'schedule': crontab(0, 0, day_of_week='1'),
        'args': ('weekly_update@gmail.com',)
    },
    'monthly_update': {
        'task': 'task.tasks.monthly_update',
        'schedule': crontab(0, 0, day_of_month='1'),
        'args': ('monthly_update@gmail.com',)
    }
}

app.conf.timezone = 'UTC'

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))