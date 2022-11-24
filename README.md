# Stock
為了股票所設計的後端 , 經由此控制API,有控制ＤＢ,前端資訊,後端資料處理 
## [Swagger API Pages](https://weikaistock.herokuapp.com/)



## API testing

[Swagger API Pages online](https://weikaistock.herokuapp.com/)


---

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


---

## 資料取得

目前資料先使用此 [finmind API](option\tools\external\stock_finmind.py) 取得開發資料並存放至[tools\external\sample_data](tools\external\sample_data)

如需要重新取得最新資訊, 重新呼叫 [finmind API](tools\external\stock_finmind.py)

說明:

1. https://blog.jiatool.com/posts/stock_finmind/

2. https://finmind.github.io/tutor/TaiwanMarket/Derivative/

3. https://github.com/FinMind/FinMind

4. https://finmindtrade.com/

---

## 頁面呈現

使用 Pyecharts 進行繪圖

---


## How to run

* [Run in develop](wiki/develop.md)
* [Run in Docker](wiki/docker.md)
* [Depoly Cloud Platform](wiki/depoly.md)

