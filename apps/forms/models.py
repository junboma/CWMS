from django.db import models

# Create your models here.

from ckeditor.fields import RichTextField  # 文本编辑器
from ckeditor_uploader.fields import RichTextUploadingField  # 富文本可上传图片

class Forms(models.Model):
    """
    考评表模板
    """
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=400, verbose_name="考评表名称", help_text='考评表名称')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        db_table = "table_forms"
        verbose_name_plural = verbose_name = '考评表'
        # ordering = ("-create_datetime",)

    def __str__(self):
        return self.name

class Points(models.Model):
    """
    扣分表
    """
    # id = models.AutoField(primary_key=True)
    forms = models.ForeignKey(to="Forms", verbose_name="关联考评表", on_delete=models.PROTECT, db_constraint=False, null=True, blank=True, help_text="关联考评表")
    points = models.CharField(max_length=800, null=True, blank=True, verbose_name="扣分点")

    class Meta:
        db_table = "table_points"
        verbose_name_plural = verbose_name = '扣分点'
        # ordering = ("-create_datetime",)

    def __str__(self):
        return self.points