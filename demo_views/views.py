from django.shortcuts import render
# Create your views here.
import json
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from pyecharts.charts import Bar, Pie
from pyecharts.faker import Faker
from pyecharts import options as opts
from v1.models import ClassifyType, CompanyProfile
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

def pie(type_amount:int=50):
    classify_type_list = ClassifyType.objects.all()[0:7].values_list('name','id')
    classify_type_zip = list( zip(*classify_type_list))
    ids_list = classify_type_zip[1]
    counts_list = [ len(CompanyProfile.objects.filter(major_type=i)) for i in ids_list]
    classify_type_company_list = list(zip(list( zip(*classify_type_list))[0], counts_list ))
    classify_type_company_list.sort(key=lambda x: (x[1]),reverse=True)
    # print()
    # [0:type_amount]
    # classify_type_company_list = list( zip(list( zip(*classify_type_list))[0], counts_list ))
    c = (
        Pie()
            .add("", classify_type_company_list[0:int(type_amount)])
            # .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])\
            .set_global_opts(title_opts=opts.TitleOpts(title="公司類型"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}間"))
            .dump_options_with_quotes()
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