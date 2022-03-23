# Developer

## How to install by develop

1. Download all related softwares

    * [Python=3.8](https://www.python.org/downloads/)
        * {PROJECT_PATH}/stock/$ ```pip install vurtualenv```

    * [PostgreSQL](https://www.postgresql.org/download/)
        * {PROJECT_PATH}/stock/$ ```.\psql -U postgres```

        * postgres=# ```create user '<YOUR_USERNAME>' with encrypted password '<YOUR_PASSWORD>';```
        
        * postgres=# ```create database '<YOUR_DBNAME>' with owner '<YOUR_USEENAME>' encoding 'UTF8';```

        * postgres=# ```\q```


2.  {PROJECT_PATH}/stock/$
    ```virtualenv env```
    >create virtual envitoment

3.  {PROJECT_PATH}/stock/$
    ```source env/bin/activate```
    >enter virtual environment

4.  {PROJECT_PATH}/stock/$
    ```pip install -r requirements.txt```
    >via requirements.txt install library

5.  add config.json in {PROJECT_PATH}/stock/[config.json](..\config.json)

```
{
    "SECRET_KEY": "lnv50535!l8ks=0p!=mamr_y)^-3x&91+p-f&f@f63v3k(6c-(",
    "DB_ENGINE" : "django.db.backends.postgresql_psycopg2",
    "DB_NAME":  "YOUR_DBNAME",
    "DB_USERNAME": "YOUR_USERNAME",
    "DB_PASSWORD" : "YOUR_PASSWORD",
    "DB_HOST" :"127.0.0.1",
    "DB_PORT" :"5432"
}
```

6.  {PROJECT_PATH}/stock/$ 
    ```python manage.py makemigrations```

7.  {PROJECT_PATH}/stock/$ 
    ```python manage.py migrate```

8.  (Option){PROJECT_PATH}/stock/$ 
    ```python tools/seeds/make_data.py```
    > Create seeds

9.  {PROJECT_PATH}/stock/$ 
    ```python manage.py runserver```
    >execute backend server
