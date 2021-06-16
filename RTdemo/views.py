from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from .models import Chapter, TestValue, Parameters, Projects, Paragraph, Table, Column, Template
from django.db import models
import os


# 获取参数列表
def para_in(request):
    # cursor = connection.cursor()
    # cursor.execute(
    #     "select p.para_name,p.display_name,p.unit,c.chapter_name from rtdemo_parameters p,rtdemo_Chapter c where v.chapter_id=c.id")
    # rows = cursor.fetchall()
    # data = {"paras": rows}
    # 获取所有参数列表
    para_list = Parameters.objects.all()
    p_val_list = Parameters.objects.values_list("id", "name", "display_name", "testvalue__value", "unit"
                                                 ,"chp__name"
                                                )
    context = {"list": p_val_list}
    return render(request, "demo_page.html", context)
