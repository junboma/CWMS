from django.contrib import admin

# Register your models here.
from .models import Report, Reason
from django.apps import apps
from import_export.admin import ImportExportModelAdmin
from .resource import ReasonResource, ReportResource

# 重写一个管理类，并绑定到模型类
@admin.register(Reason)
class ReasonAdmin(ImportExportModelAdmin):
    resource_class = ReasonResource
    list_display = ('id', 'report', 'points', 'reason')
    list_display_links = ('id', 'report', 'points', 'reason')

# 重写一个管理类，并绑定到模型类
@admin.register(Report)
class ReportAdmin(ImportExportModelAdmin):
    resource_class = ReportResource
    list_display = ('id', 'name', 'datetime', 'CRH', 'score', 'usetime', 'examiner', 'is_makeup', 'count')
    list_display_links = ('id', 'name', 'datetime', 'CRH', 'score', 'usetime', 'examiner', 'is_makeup', 'count')


all_models = apps.get_app_config('report').get_models()
for model in all_models:
    try:
        admin.site.register(model)
    except:
        pass