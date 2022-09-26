from import_export import resources
from .models import Report, Reason
from forms.models import Forms, Points
from users.models import CRH, UserProfile, Examiner
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget


class ReasonResource(resources.ModelResource):
    reason = fields.Field(column_name="关联扣分原因", attribute='reason')
    report = fields.Field(column_name='统计表', attribute='report', widget=ForeignKeyWidget(Report, 'name'))
    points = fields.Field(column_name='扣分点', attribute='points', widget=ForeignKeyWidget(Points, 'points'))

    class Meta:
        model = Reason
        skip_unchanged = True  # 导入数据时，如果该条数据未修改过，则会忽略（默认根据id去匹配数据，可通过定义import_id_fields去更改）
        # fields内的模型字段会被导入导出
        # fields = ['id', 'report', 'reason']
        # exclude = ['add_time']
        # export_order（自定义） 选项设置导出字段的显式顺序，没在这里规定的就按默认顺序排在后面（不能只写一个）(导入不用管顺序)
        export_order = ('id', 'report', 'points', 'reason')
        # 下面规定联合主键，决定是update还是create，可以避免重复导入相同的记录
        import_id_fields = ['id']

class ReportResource(resources.ModelResource):
    user = fields.Field(column_name='考生', attribute='user', widget=ManyToManyWidget(UserProfile, 'name'))
    name = fields.Field(column_name='统计表', attribute='name', widget=ForeignKeyWidget(Forms, 'name'))
    datetime = fields.Field(column_name="学习日期", attribute='datetime')
    CRH = fields.Field(column_name='考试车型', attribute='CRH', widget=ForeignKeyWidget(CRH, 'name'))
    score = fields.Field(column_name="考试成绩", attribute='score')
    usetime = fields.Field(column_name="考试使用时间", attribute='usetime')
    examiner = fields.Field(column_name='考评人', attribute='examiner', widget=ForeignKeyWidget(Examiner, 'name'))
    count = fields.Field(column_name="补考次数", attribute='count')

    class Meta:
        model = Report
        skip_unchanged = True  # 导入数据时，如果该条数据未修改过，则会忽略（默认根据id去匹配数据，可通过定义import_id_fields去更改）
        # fields内的模型字段会被导入导出
        # fields = ['id', 'user', 'name', 'datetime', 'CRH', 'score', 'usetime', 'examiner', 'is_makeup', 'count']
        # exclude = ['add_time']
        # export_order（自定义） 选项设置导出字段的显式顺序，没在这里规定的就按默认顺序排在后面（不能只写一个）(导入不用管顺序)
        export_order = ('id', 'user', 'name', 'datetime', 'CRH', 'score', 'usetime', 'examiner', 'count')
        # 下面规定联合主键，决定是update还是create，可以避免重复导入相同的记录
        import_id_fields = ['id']