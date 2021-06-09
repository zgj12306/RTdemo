from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
import os

#获取参数列表
def parameter(request):
    cursor = connection.cursor()
    cursor.execute("select * from test_p")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return render(request,"demo_page.html")