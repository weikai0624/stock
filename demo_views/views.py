import copy
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q ,F
from rest_framework.views import APIView
from pyecharts.charts import Bar, Pie
from pyecharts.faker import Faker
from pyecharts import options as opts
from v1.models import ClassifyType, CompanyProfile, ObjectData
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from pyecharts.charts import Bar, Pie, Kline, Line
from datetime import datetime
from pytz import timezone

def pie(type_amount:int=50):
    classify_type_list = ClassifyType.objects.all()[0:7].values_list('name','id')
    classify_type_zip = list( zip(*classify_type_list))
    ids_list = classify_type_zip[1]
    counts_list = [ len(CompanyProfile.objects.filter(major_type=i)) for i in ids_list]
    classify_type_company_list = list(zip(list( zip(*classify_type_list))[0], counts_list ))
    classify_type_company_list.sort(key=lambda x: (x[1]),reverse=True)
    c = (
        Pie()
            .add("", classify_type_company_list[0:int(type_amount)])
            # .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])\
            .set_global_opts(title_opts=opts.TitleOpts(title="公司類型"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}間"))
            .dump_options_with_quotes()
    )
    return c

def kline(symbol):
    tz=timezone('Asia/Taipei') 
    datetime_format = "%Y%m%d %H%M"
    # symbol='2330'
    company = CompanyProfile.objects.get(symbol=symbol)
    company_data = ObjectData.objects.filter(company=company).order_by('data_time')
    data_time_list = company_data.values_list('data_time')
    data_date_set_list = sorted( list( set(map(lambda x: x[0].strftime(datetime_format), data_time_list) )) )

    date_time_price = []
    for one in data_date_set_list:
        one_data_time = datetime.strptime(one, datetime_format)
        filter_ = {
            'data_time__year': one_data_time.year,
            'data_time__month': one_data_time.month,
            'data_time__day': one_data_time.day,
            'data_time__hour': one_data_time.hour,
            'data_time__minute': one_data_time.minute
        }
        date_time_price.append([ i[0] for i in company_data.filter(**filter_).values_list('price')] )
    # 轉換成台灣時間
    data_date_list_tz = list(map(lambda x: datetime.strptime(x, datetime_format).astimezone(tz).strftime(datetime_format), data_date_set_list))
    c = (
        Kline()
            .add_xaxis(data_date_list_tz)
            .add_yaxis(company.name, date_time_price)
            .set_global_opts(
                title_opts=opts.TitleOpts(title=f'公司:{company.name}的K線圖', subtitle=f'代號:{company.symbol}'),
                yaxis_opts=opts.AxisOpts(is_scale=True),
                xaxis_opts=opts.AxisOpts(is_scale=True),
            )
            # .dump_options_with_quotes()
            .render_embed()
            # .render('kline.html')
        )
   
    return c

class PieView(APIView):
    '''
    取得公司的分類類型數量, 並render 大餅圖
    '''
    @swagger_auto_schema(   
        operation_summary='公司類型分類數量',
        operation_description='公司類型分類數量',
        manual_parameters=[
            openapi.Parameter('type_amount', openapi.IN_QUERY, description="前N多類型", type=openapi.TYPE_STRING, default=7),
        ]
    )
    def get(self, request, *args, **kwargs):
        type_amount = request.GET.get('type_amount',"")
        print(type_amount)
        context = {"data": json.dumps(json.loads(pie(type_amount)))}
        return render(request, 'pie.html', context)

class KlineView(APIView):
    @swagger_auto_schema(   
        operation_summary='k線圖',
        operation_description='k線圖',
        manual_parameters=[
            openapi.Parameter('symbol', openapi.IN_QUERY, description="代號", type=openapi.TYPE_STRING, default=2330),
        ]
    )
    def get(self, request, *args, **kwargs):
        symbol = request.GET.get('symbol',"")
        # symbol = '2330'
        return HttpResponse(kline(symbol))