# Package

Use [Docker](https://www.docker.com/) to package all the project.
[Docker celery](https://soshace.com/dockerizing-django-with-postgres-redis-and-celery/)
[Docker celery](https://testdriven.io/blog/django-celery-periodic-tasks/)

1. Download all related softwares
    * [Docker](https://www.docker.com/)
2. setting backend infotmations in Docker

    * [docker-compose.yml](../docker-compose.yml)

    * [Dockerfile](../Dockerfile)

3.  {PROJECT_PATH}/stock/$
    ```docker build -t stock_backend .```

4.  {PROJECT_PATH}/stock/$
    ```docker-compose build ```
    >

5.  {PROJECT_PATH}/stock/$
    ```docker-compose up```

