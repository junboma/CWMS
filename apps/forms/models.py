from django.db import models

# Create your models here.

from ckeditor.fields import RichTextField  # 文本编辑器
from ckeditor_uploader.fields import RichTextUploadingField  # 富文本可上传图片

class Forms(models.Model):
    """
    考评表模板
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="考评表名称", help_text='商品名称')
    points1 = models.CharField(max_length=32, null=True, blank=True, verbose_name="扣分点1")
    reason1 = models.CharField(max_length=200, null=True, blank=True, verbose_name="扣分原因1")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        db_table = "table_forms"
        verbose_name_plural = verbose_name = '考评表'
        # ordering = ("-create_datetime",)

    def __str__(self):
        return self.name