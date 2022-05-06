from celery import Celery
from celery.schedules import crontab
# from backend.celery import app as celery_app
from django.conf import settings
from tools.external.stock_finmind import FinMind
from celery import shared_task
from v1.models import CompanyProfile
'''
https://hackmd.io/@shaoeChen/rJELMAEwm?type=view
'''

app = Celery()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )


@shared_task
def test(arg):
    print(arg)

@shared_task
def add(x, y):
    z = x + y
    print(z)

@shared_task
def per_test():
    print("123123123123")
    return "test"