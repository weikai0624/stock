web: gunicorn backend.wsgi --log-file -
celery: celery -A backend.celery worker --pool=solo -l info