import time
from celery.schedules import crontab
# from backend.celery import app as celery_app
from celery import Celery
from django.conf import settings
from tools.external.stock_finmind import FinMind
from celery import shared_task
from v1.models import CompanyProfile
'''
https://hackmd.io/@shaoeChen/rJELMAEwm?type=view
'''

app=Celery()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )


@shared_task
def test(arg):
    print(arg)