from django.db import models
from django.contrib.auth.models import User


class Chapter(models.Model):
    name = models.CharField('章节名', max_length=100)
    layer = models.IntegerField('层级')
    order = models.IntegerField('排序', default=0)
    parent_id = models.IntegerField('父级', null=True, blank=True)


class Parameters(models.Model):
    name = models.CharField('参数名', max_length=50)
    display_name = models.CharField('参数中文名', max_length=100)
    unit = models.CharField('单位', max_length=10, null=True, blank=True)
    chp_id = models.ForeignKey(Chapter, on_delete=models.CASCADE, db_index=True)
