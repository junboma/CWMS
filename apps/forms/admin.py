from django.contrib import admin

# Register your models here.

from .models import Forms
from django.apps import apps

all_models = apps.get_app_config('forms').get_models()
for model in all_models:
    try:
        admin.site.register(model)
    except:
        pass