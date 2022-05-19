# Stock
為了股票所設計的後端 , 經由此控制API,有控制ＤＢ,前端資訊,後端資料處理 
## [Swagger API Pages](https://weikaistock.herokuapp.com/)


目前資料先使用此 [finmind API 取得 ](option\tools\external\stock_finmind.py)
說明:
```
https://blog.jiatool.com/posts/stock_finmind/
https://finmind.github.io/tutor/TaiwanMarket/Derivative/
https://github.com/FinMind/FinMind
https://finmindtrade.com/
```

並使用 Pyecharts 進行繪圖

## Use package
* Framework

    * [Django](https://www.djangoproject.com/) 
        * [rest framework](https://www.django-rest-framework.org/)
        * [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) swagger
        * [celery](https://docs.celeryq.dev/en/stable/index.html)
        * [redis](https://github.com/redis/redis-py)

* Database
    * [PostgreSQL](https://www.postgresql.org/)
    * [Redis](https://redis.io/)
        > for Window download [LINK](https://github.com/MicrosoftArchive/redis/releases)

## How to run

* [Run in develop](wiki/develop.md)
* [Run in Docker](wiki/docker.md)
* [Depoly in Heroku](wiki\heroku.md)
