from import_export import resources
from .models import Forms, Points
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

class FormsResource(resources.ModelResource):
    name = fields.Field(column_name="考评表名称", attribute='name')
    # points = fields.Field(column_name='关联扣分点', attribute='points', widget=ForeignKeyWidget(Points, 'points'))

    class Meta:
        model = Forms
        skip_unchanged = True  # 导入数据时，如果该条数据未修改过，则会忽略（默认根据id去匹配数据，可通过定义import_id_fields去更改）
        # fields内的模型字段会被导入导出
        # fields = ['id', 'name']
        exclude = ['add_time']
        # export_order（自定义） 选项设置导出字段的显式顺序，没在这里规定的就按默认顺序排在后面（不能只写一个）(导入不用管顺序)
        export_order = ('id', 'name')
        # 下面规定联合主键，决定是update还是create，可以避免重复导入相同的记录
        import_id_fields = ['id']

class PointsResource(resources.ModelResource):
    forms = fields.Field(column_name='考评表名称', attribute='forms', widget=ForeignKeyWidget(Forms, 'name'))
    points = fields.Field(column_name="关联扣分点", attribute='points')

    class Meta:
        model = Points
        skip_unchanged = True  # 导入数据时，如果该条数据未修改过，则会忽略（默认根据id去匹配数据，可通过定义import_id_fields去更改）
        # fields内的模型字段会被导入导出
        fields = ['id', 'forms', 'points']
        # exclude = ['add_time']
        # export_order（自定义） 选项设置导出字段的显式顺序，没在这里规定的就按默认顺序排在后面（不能只写一个）(导入不用管顺序)
        export_order = ('id', 'forms', 'points')
        # 下面规定联合主键，决定是update还是create，可以避免重复导入相同的记录
        import_id_fields = ['id']