from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import NewUser


# Register your models here.

class NewUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email', 'first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'roles')}),
        (_('Important dates'), {'fields': ('date_joined',)}),
    )

    list_display = ('id', 'username', 'roles', 'email', 'is_active', 'last_login', 'code')
    list_display_links = ('id', 'username', 'roles', 'email', 'last_login')
    search_fields = ('username', 'email')


admin.site.register(NewUser, NewUserAdmin)


from .models import UserProfile, VerifyCode, Post, Dept, Workshop
from django.apps import apps

from import_export.admin import ImportExportModelAdmin
from .resource import UserProfileResource, PostResource, DeptResource, WorkshopResource


# 重写一个管理类，并绑定到模型类
@admin.register(UserProfile)

class UserProfileAdmin(ImportExportModelAdmin):
    # pass
    resource_class = UserProfileResource
    list_display = ('id', 'name', 'job_id', 'is_keypeople', 'birthday', 'mobile', 'gender', 'post', 'dept', 'workshop', 'railway_sections', 'status')
    list_display_links = ('id', 'name', 'job_id', 'is_keypeople', 'birthday', 'mobile', 'gender', 'post', 'dept', 'workshop', 'railway_sections', 'status')
    search_fields = ('name', 'job_id')
#
# admin.site.register(UserProfile, UserProfileAdmin)
# 重写一个管理类，并绑定到模型类
@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    pass
# 重写一个管理类，并绑定到模型类
@admin.register(Dept)
class DeptAdmin(ImportExportModelAdmin):
    resource_class = DeptResource
    list_display = ('id', 'name', 'sort', 'owner', 'phone', 'email', 'status')
    list_display_links = ('id', 'name', 'sort', 'owner', 'phone', 'email', 'status')

# 重写一个管理类，并绑定到模型类
@admin.register(Workshop)
class WorkshopAdmin(ImportExportModelAdmin):
    resource_class = WorkshopResource
    list_display = ('id', 'name', 'sort', 'owner', 'phone', 'email', 'status')
    list_display_links = ('id', 'name', 'sort', 'owner', 'phone', 'email', 'status')

all_models = apps.get_app_config('users').get_models()
for model in all_models:
    try:
        admin.site.register(model)
    except:
        pass
