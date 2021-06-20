from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from .models import Chapter, TestValue, Parameters, Projects, Paragraph, Table, Column, Template, TestValue, \
    ParameterValue
from RTdemo.common.response import json_response, json_error, read_file
from django.db import models
from django.db.models import Q
import os


# 获取参数列表
def para_in(request):
    # cursor = connection.cursor()
    # cursor.execute(
    #     "select p.para_name,p.display_name,p.unit,c.chapter_name from rtdemo_parameters p,rtdemo_Chapter c where v.chapter_id=c.id")
    # rows = cursor.fetchall()
    # data = {"paras": rows}
    # 获取所有参数列表
    # 有参数对应的章节ID
    q = None
    if 'q' in request.GET:
        q = request.GET['q']
        p_val_list = Parameters.objects.filter(chp_id=q).values("id", "name", "display_name", "testvalue__value",
                                                                "unit")
    else:
        # para_list = Parameters.objects.all()
        p_val_list = Parameters.objects.values("id", "name", "display_name", "testvalue__value", "testvalue__id",
                                               "unit")
    values = filter_none(p_val_list)
    context = {"list": values}

    return render(request, "demo_page.html", context)


def save_parameter(request):
    if request.POST:
        # data = eval(data) #如果前端用了serializeStr的話需要
        tv=TestValue.objects.get(id=request.POST['id'])
        tv.value=request.POST['value']
        # value = TestValue(id=request.POST['id'], parameter_id=request.POST['parameter'], value=request.POST['value'])
        # value = ParameterValue(parameter=data.parameter, value=data.value)
        tv.save()
        # TestValue.objects.create(value)
    # ParameterValue.objects.create(value)
    return json_response('保存成功！')


# 避免前端出現none相關的錯誤
def filter_none(values):
    ret = []
    for row in values:
        for key in row:
            if row[key] is None:
                row[key] = ''
            else:
                row[key]
        ret.append(row)
    return ret
