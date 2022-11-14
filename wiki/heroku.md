
# How to deploy in heroku

## First Time
> heroku setting [Procfile](..\Procfile)
1. you need to register [heroku](https://dashboard.heroku.com/)
2. create heroku app {appname}
3. create 'Heroku Postgres Hobby Dev' (Starting November 28th, 2022, free dynos will no longer be available)
4. create 'Heroku Data for Redis Hobby Dev' (Starting November 28th, 2022, free dynos will no longer be available)
5. set config in {PROJECT_PATH}/stock/[config.json](..\config.json)
6. ```heroku login```
7. ```heroku git:remote -a {appname}```
8. ```heroku config:set DJANGO_SETTINGS_MODULE=backend.settings```
9. ```git push heroku <branchname>:main```
    > push local branch to heroku main to depoly
10. ```heroku ps:scale web=1```
11. ```heroku run python manage.py migrate```
12. ```heroku run python tools/seeds/make_data.py```

## Update Depoly
1. ```heroku login```
2. ```heroku config:set DJANGO_SETTINGS_MODULE=backend.settings```
3. ```git push heroku <branchname>:main```
    > push local ```<branchname>``` to heroku main to depoly
