# Depoly

## How to depoly in fly.io:

reference
*  [https://testdriven.io/blog/django-fly/](https://testdriven.io/blog/django-fly/)
*  [https://github.com/tomwojcik/django-fly.io-example-project](https://github.com/tomwojcik/django-fly.io-example-project)
*  [https://fly.io/docs/reference/redis/](https://fly.io/docs/reference/redis/)


### requirements

1. [Flyctl](https://fly.io/docs/flyctl/installing/)

### Step
1.  ```$ flyctl auth login```
    > to create account and log in 


1. ```$ flyctl launch```
    
    * Would you like to copy its configuration to the new app? (y/N) : y
    * Overwrite "D:\stock\Dockerfile"? : n
    * App Name (leave blank to use an auto-generated name): app_name
    * Select region: hkg
    * Would you like to set up a Postgresql database now? (y/N) : y
        > Development - Single node, 1x shared CPU, 256MB RAM, 1GB disk (Free)
    * Postgres cluster app_name-db created
  Username:    postgres
  Password:    password
  Hostname:    kapp_name-db.internal
  Proxy Port:  5432
  PG Port: 5433
    ```
    The following secret was added to kk-stock:
    DATABASE_URL=postgres://app_name:....app_name-db.internal:5432/app_name
    ```

  launch success

1. if database does not create, ```$ flyctl pg create```
    ```
    ? Choose an app name (leave blank to generate one): kk-stock-db
    automatically selected personal organization: weikai860624@gmail.com
    ? Select region: Hong Kong, Hong Kong (hkg)
    ? Select configuration: Development - Single node, 1x shared CPU, 256MB RAM, 1GB disk
    ```

1. ```$ flyctl redis create```
    ```
    Your Upstash Redis database redis_name is ready.
    Apps in the personal org can connect to at redis://default:XXXX.upstash.io
    If you have redis-cli installed, use fly redis connect to connect to your database.
    ```

1. ```$ flyctl apps list```
    > to look your app

1. ```$ flyctl status```
    > to watch your app status
    ```
    App
    Name     = app_name
    Owner    = personal
    Version  = 0
    Status   = pending
    Hostname = app_name.fly.dev
    Platform =
    ```


1. add environments setting in system environments (named 'Secrets' in fly.io)

    ```$ flyctl secrets set DEBUG='1'```

    ```$ flyctl secrets set ALLOWED_HOSTS='*'```

    ```$ flyctl secrets set DATABASE_URL='postgres://postgres:password@kk-stock-db.internal:5432/kk-stock'```

    ```$ flyctl secrets set CELERY_BROKER_URL='redis://default:XXXX.upstash.io'```

    ```$ flyctl secrets set CELERY_RESULT_BACKEND='redis://default:XXXX.upstash.io'```

    ```$ flyctl secrets set CSRF_TRUSTED_ORIGINS='https://app_name.fly.dev'```

    ```$ fly secrets set SECRET_KEY='django-insecure-qmq4l#2)h9_!us=2^kw6n&rs$=-wbckvn=$k-2(asbcsf!mey2'```

    ```$ flyctl secrets set EMAIL_HOST='smtp.gmail.com' ```

    ```$ flyctl secrets set EMAIL_PORT='587' ```

    ```$ flyctl secrets set EMAIL_HOST_USER='XXXX@gmail.com' ```

    ```$ flyctl secrets set EMAIL_HOST_PASSWORD='password' ```

1. ```$ flyctl secrets list```
    > Check environments setting(Secrets in fly.io)

1. ```$ fly deploy ```
    > depoly

1. ```$ fly status```
    > to watch your app status

1. ```$ fly logs```
    > watch logs








### problem

1. non interactive (in Windows)
    ```
    $fly redis create
    automatically selected personal organization: xxxxx@gmail.com
    Error prompt: non interactive
    ```
    use 
    [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-us&gl=us) to ```$ fly redis create``` again
