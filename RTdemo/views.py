from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
import os

#获取参数列表
def para_in(request):
    cursor = connection.cursor()
    cursor.execute("select p.para_name,p.display_name,p.unit,c.chapter_name from test_p p,chapter c where p.chapter_id=c.idchapter")
    rows = cursor.fetchall()
    data={"paras":rows}
    return render(request,"demo_page.html",context=data)