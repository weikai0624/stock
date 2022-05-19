
# How to deploy in heroku

1. ```git init ```
2. ```heroku git:remote -a weikaistock```
    >git remote -v 
3. ```heroku config:set DJANGO_SETTINGS_MODULE=backend.settings```
4. ```git push heroku <branchname>:main```
5. ```heroku ps:scale web=1```
6. ```heroku run python manage.py migrate```
7. ```heroku run python tools/seeds/make_data.py```
