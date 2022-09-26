from django.contrib import admin

# Register your models here.

from .models import Forms, Points
from django.apps import apps

from import_export.admin import ImportExportModelAdmin
from .resource import FormsResource, PointsResource

# 重写一个管理类，并绑定到模型类
@admin.register(Forms)
class FormsAdmin(ImportExportModelAdmin):
    resource_class = FormsResource
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

# 重写一个管理类，并绑定到模型类
@admin.register(Points)
class PointsAdmin(ImportExportModelAdmin):
    resource_class = PointsResource
    list_display = ('id', 'forms', 'points')
    list_display_links = ('id', 'forms', 'points')

all_models = apps.get_app_config('forms').get_models()
for model in all_models:
    try:
        admin.site.register(model)
    except:
        pass