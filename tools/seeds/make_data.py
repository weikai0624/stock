import os
import sys
import json
import django
from datetime import datetime


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stock.settings")
django.setup()

from django.conf import settings
from v1.models import UserProfile,GroupProfile,Project,CompanyProfile,ObjectData,ClassifyType
from django.contrib.auth.models import User,Group

from external.stock_finmind import FinMind


CONFIG = settings.CONFIG
FIN_TOKEN = settings.CONFIG.get("FIN_TOKEN",'')

def read_json(path):
    with open (path, 'r') as F :
        return json.load(F)

def create_objects_data(objects_data):
    objects_data_list = []
    for i in objects_data:
        data_time = datetime.strptime( i['date']+i['Time']+"+0800", '%Y-%m-%d%H:%M:%S.%f%z')
        date_time_= data_time.strftime('%Y-%m-%dT%H:%M:%S.%f%Z') 
        data = {
            "company": CompanyProfile.objects.get(symbol=i['stock_id']),
            "status" :i['TickType'],
            "price":i['deal_price'],
            "mount":i['volume'],
            "data_time":data_time
        }
        objects_data_list.append(ObjectData(**data))
    return objects_data_list

def create_classify_type(compony_info):
    classify_type_set = set(map(lambda x: x['industry_category'], compony_info))
    classify_type_list = []
    for i in classify_type_set:
        data = {
            "name": i
        }
        classify_type_list.append(ClassifyType(**data))
    return classify_type_list

def create_company(compony_info):
    change_data_key = []
    check = []
    for i in compony_info:
        if i["stock_name"] in check:
            continue
        data = {
            "name": i.get("stock_name",""),
            "symbol": i.get("stock_id",""),
            "description":  i.get("stock_name","") + i.get("stock_id",""),
        }
        check.append(i['stock_name'])
        change_data_key.append(CompanyProfile(**data))
    return change_data_key
    
def delete_table_data(table_name):
    table_name.objects.all().delete()


def delete_seeds(delete_bool):
    if delete_bool:
        delete_table_data(ObjectData)
        delete_table_data(CompanyProfile)
        delete_table_data(ClassifyType)

def create_seeds(create_bool):
    # all_info_data = FinMind(FIN_TOKEN).all_info()
    all_compony_info_data = read_json('..\\external\sample_data\\TaiwanStockInfo.json')
    classify_type_data = create_classify_type(all_compony_info_data)
    ClassifyType.objects.bulk_create(classify_type_data)

    company_data = create_company(all_compony_info_data)
    CompanyProfile.objects.bulk_create(company_data)

    one_compony_info_data = read_json('..\\external\sample_data\\ALL.json')
    objects_data = create_objects_data(one_compony_info_data)
    ObjectData.objects.bulk_create(objects_data)


def Main():
    delete_seeds(True)
    create_seeds(True)

if __name__ == "__main__":
    Main()

    pass