from django.db import models

# Create your models here.

from forms.models import Forms, Points
from users.models import UserProfile, CRH, Examiner
from django.contrib.auth import get_user_model

User = get_user_model()

class Report(models.Model):
    """
    统计表单填写
    """
    id = models.AutoField(primary_key=True)
    user = models.ManyToManyField(UserProfile, verbose_name='考生', help_text='考生')
    name = models.ForeignKey(Forms, verbose_name="统计表名称", help_text="统计表名称", on_delete=models.CASCADE)
    datetime = models.DateTimeField(verbose_name="学习日期")
    CRH = models.ForeignKey(CRH, verbose_name="考试车型", help_text="考试车型", on_delete=models.CASCADE)
    score = models.IntegerField(verbose_name="考试成绩")
    usetime = models.CharField(verbose_name="考试使用时间", max_length=100, help_text="XX分XX秒")
    examiner = models.ForeignKey(Examiner, verbose_name="考评人", help_text="考评人", on_delete=models.CASCADE)
    is_makeup = models.BooleanField(default=False, verbose_name="是否补考", help_text="是否补考")
    count = models.IntegerField(verbose_name="补考次数", default=0)

    class Meta:
        db_table = "table_report"
        verbose_name_plural = verbose_name = '统计表'
        ordering = ("id",)

    def __str__(self):
        return str(self.name)

class Reason(models.Model):
    id = models.AutoField(primary_key=True)
    report = models.ForeignKey(to="Report", verbose_name="关联统计表", on_delete=models.PROTECT, db_constraint=False,
                              null=True, blank=True, help_text="关联统计表")
    points = models.ForeignKey(Points, verbose_name="关联扣分点", on_delete=models.PROTECT, db_constraint=False,
                              null=True, blank=True, help_text="关联扣分点")
    # points = models.CharField(max_length=800, null=True, blank=True, verbose_name="扣分点")
    reason = models.CharField(max_length=600, null=True, blank=True, verbose_name="扣分原因")

    class Meta:
        db_table = "table_reason"
        verbose_name_plural = verbose_name = '扣分原因'
        ordering = ("id",)

    def __str__(self):
        return self.reason