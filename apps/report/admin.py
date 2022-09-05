from django.contrib import admin

# Register your models here.

from django.apps import apps

all_models = apps.get_app_config('report').get_models()
for model in all_models:
    try:
        admin.site.register(model)
    except:
        pass