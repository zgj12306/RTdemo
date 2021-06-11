from django.db import models
import MySQLdb

class Test_p(models.Model):
    para_name = models.CharField('参数名', max_length=45, null=False, blank=True, unique=True)
    display_name = models.CharField('显示名', max_length=45, null=False, blank=True, unique=True)
    unit = models.CharField('单位', max_length=10, null=False, blank=True)
    chapter_id = models.IntegerField('章节ID', null=False, blank=True, unique=True)

    def __str__(self):
        return self.para_name


