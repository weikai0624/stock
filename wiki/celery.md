# Celery

## How to Start: 
* celery -A backend.celery worker --pool=solo -l info
* celery -A backend.celery worker -l info
* celery -A backend.celery beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler