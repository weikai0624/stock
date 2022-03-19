# Stock
為了股票所設計的後端 , 經由此控制API,有控制ＤＢ,前端資訊,後端資料處理 

目前資料先使用此 [finmind API 取得 ](option\tools\external\stock_finmind.py)
說明:
https://blog.jiatool.com/posts/stock_finmind/
https://finmind.github.io/tutor/TaiwanMarket/Derivative/
https://github.com/FinMind/FinMind
https://finmindtrade.com/

並使用 Pyecharts 進行繪圖

## Install

1.  {PROJECT_PATH}/stock/ 
    ```virtualenv env``
    
    
2.  {PROJECT_PATH}/stock/$ 
    ```pip install -r requirements.txt```
    >via requirements.txt install library

3.  {PROJECT_PATH}/stock/$ 
    ```source/env/bin/activate```
    >enter virtual environment
 
4.  add config.json in stock/config.json
```
{
    "SECRET_KEY": "lnv50535!l8ks=0p!=mamr_y)^-3x&91+p-f&f@f63v3k(6c-(",
    "DB_ENGINE" : "django.db.backends.postgresql_psycopg2",
    "DB_NAME":  "db_name",
    "DB_USERNAME": "postgres",
    "DB_PASSWORD" : "password",
    "DB_HOST" :"127.0.0.1",
    "DB_PORT" :"5432"
}
```

5.  {PROJECT_PATH}/stock/$ 
    ```python manage.py runserver```
    >execute backend server
