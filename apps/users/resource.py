from import_export import resources
from .models import UserProfile, Post, Dept, Workshop, Railway_sections, CRH
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from django.apps import apps

class UserProfileResource(resources.ModelResource):
    # def __init__(self):
    #     super(UserProfileResource, self).__init__()
    #     # 获取所以字段的verbose_name并存放在字典
    #     field_list = apps.get_model('users', 'UserProfile')._meta.fields
    #     self.vname_dict = {}
    #     for i in field_list:
    #         self.vname_dict[i.name] = i.verbose_name
    #
    # # 默认导入导出field的column_name为字段的名称，这里修改为字段的verbose_name
    # def get_export_fields(self):
    #     fields = self.get_fields()
    #     for field in fields:
    #         field_name = self.get_field_name(field)
    #         # 自定义导出字段里可能有关联关系，但vname_dict肯定没有双下划线，所以必须处理
    #         if field_name.find("__") > 0:
    #             # 如果是关联关系的，只取字段名，不找关联，因为关联内容不在vname_dict里
    #             field_name = field_name.split("__")[0]
    #         # 如果此字段有verbose_name，就用
    #         if field_name in self.vname_dict.keys():
    #             field.column_name = self.vname_dict[field_name]
    #     return fields
    name = fields.Field(column_name="姓名", attribute='name')
    job_id = fields.Field(column_name="工号", attribute='job_id')
    birthday = fields.Field(column_name="生日", attribute='birthday')
    mobile = fields.Field(column_name="手机号", attribute='mobile')
    # is_keypeople = fields.Field(column_name="是否关键人", attribute='is_keypeople')
    gender = fields.Field(column_name="性别", attribute='get_gender_display')
    status = fields.Field(column_name="在职状态", attribute='get_status_display')
    # 给Resource添加一个自定义字段，指向模型的关系对象，用widget做格式规范
    post = fields.Field(column_name='关联岗位', attribute='post', widget=ForeignKeyWidget(Post, 'name'))
    CRH = fields.Field(column_name='关联车型资质', attribute='CRH', widget=ManyToManyWidget(CRH, ',', 'name'))
    dept = fields.Field(column_name='所属班组', attribute='dept', widget=ForeignKeyWidget(Dept, 'name'))
    workshop = fields.Field(column_name='所属车间', attribute='workshop', widget=ForeignKeyWidget(Workshop, 'name'))
    railway_sections = fields.Field(column_name='所属站段', attribute='railway_sections', widget=ForeignKeyWidget(Railway_sections, 'name'))

    class Meta:
        model = UserProfile
        skip_unchanged = True  # 导入数据时，如果该条数据未修改过，则会忽略（默认根据id去匹配数据，可通过定义import_id_fields去更改）
        # fields内的模型字段会被导入导出
        # fields = ['name', 'job_id', 'birthday', 'mobile', 'gender', 'post', 'CRH', 'dept', 'workshop', 'railway_sections',]
        # exclude = ['id']
        # export_order（自定义） 选项设置导出字段的显式顺序，没在这里规定的就按默认顺序排在后面（不能只写一个）(导入不用管顺序)
        export_order = ('id', 'name', 'job_id', 'birthday', 'mobile', 'gender', 'post', 'CRH', 'dept', 'workshop', 'railway_sections', 'status')
        # 下面规定联合主键，决定是update还是create，可以避免重复导入相同的记录
        import_id_fields = ['name']

class PostResource(resources.ModelResource):

    class Meta:
        model = Post
        skip_unchanged = True  # 导入数据时，如果该条数据未修改过，则会忽略（默认根据id去匹配数据，可通过定义import_id_fields去更改）
        # fields内的模型字段会被导入导出
        # export_order（自定义） 选项设置导出字段的显式顺序，没在这里规定的就按默认顺序排在后面（不能只写一个）(导入不用管顺序)
        export_order = ('id', 'name')
        # 下面规定联合主键，决定是update还是create，可以避免重复导入相同的记录
        import_id_fields = ['name', ]


class DeptResource(resources.ModelResource):
    class Meta:
        model = Dept
        skip_unchanged = True  # 导入数据时，如果该条数据未修改过，则会忽略（默认根据id去匹配数据，可通过定义import_id_fields去更改）
        # fields内的模型字段会被导入导出
        # export_order（自定义） 选项设置导出字段的显式顺序，没在这里规定的就按默认顺序排在后面（不能只写一个）(导入不用管顺序)
        export_order = ('id', 'name')
        # 下面规定联合主键，决定是update还是create，可以避免重复导入相同的记录
        import_id_fields = ['name', ]


class WorkshopResource(resources.ModelResource):
    class Meta:
        model = Workshop
        skip_unchanged = True  # 导入数据时，如果该条数据未修改过，则会忽略（默认根据id去匹配数据，可通过定义import_id_fields去更改）
        # fields内的模型字段会被导入导出
        # export_order（自定义） 选项设置导出字段的显式顺序，没在这里规定的就按默认顺序排在后面（不能只写一个）(导入不用管顺序)
        export_order = ('id', 'name')
        # 下面规定联合主键，决定是update还是create，可以避免重复导入相同的记录
        import_id_fields = ['name', ]