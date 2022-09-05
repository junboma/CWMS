from django.db import models

# Create your models here.

from forms.models import Forms
from django.contrib.auth import get_user_model

User = get_user_model()

class Report(models.Model):
    """
    统计表单填写
    """
    id = models.AutoField(primary_key=True)
    user = models.ManyToManyField(User, verbose_name='用户', help_text='用户')
    name = models.ForeignKey(Forms, verbose_name="统计表名称", help_text="统计表名称", on_delete=models.CASCADE)
    datetime = models.DateTimeField(verbose_name="学习日期")
    CRH = models.CharField(verbose_name="考试车型", max_length=32)
    score = models.IntegerField(verbose_name="考试成绩")
    usetime = models.DateTimeField(verbose_name="考试使用时间", auto_now_add=True)
    examiner = models.CharField(verbose_name="考评人", max_length=32)
    is_makeup = models.BooleanField(default=False, verbose_name="是否补考", help_text="是否补考")
    count = models.IntegerField(verbose_name="补考次数")

    class Meta:
        db_table = "table_report"
        verbose_name_plural = verbose_name = '统计表'
        # ordering = ("-create_datetime",)

    def __str__(self):
        return self.name