FROM python:3.8
LABEL maintainer="weikai860624@gmail.com"


WORKDIR /stock
COPY . /stock/

RUN pip install -r requirements.txt

WORKDIR /stock

VOLUME /stock
EXPOSE 8000

ENTRYPOINT [ "/bin/bash", "docker-entrypoint.sh" ]
CMD python manage.py runserver 0.0.0.0:8000