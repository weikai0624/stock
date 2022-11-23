FROM python:3.8
LABEL maintainer="weikai860624@gmail.com"
RUN apt-get update -qq && apt-get install -y postgresql-client

WORKDIR /stock
COPY . /stock/

RUN pip install -r requirements.txt

WORKDIR /stock

VOLUME /stock
EXPOSE 8000

ENTRYPOINT [ "/bin/bash", "docker-entrypoint.sh" ]
# CMD python manage.py runserver 0.0.0.0:8000

# expose port 8000
# EXPOSE 8000

# CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "backend.wsgi:application"]
