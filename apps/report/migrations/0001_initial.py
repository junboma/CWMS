# Generated by Django 4.1 on 2022-09-18 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(verbose_name='学习日期')),
                ('CRH', models.CharField(max_length=32, verbose_name='考试车型')),
                ('score', models.IntegerField(verbose_name='考试成绩')),
                ('usetime', models.DateTimeField(auto_now_add=True, verbose_name='考试使用时间')),
                ('examiner', models.CharField(max_length=32, verbose_name='考评人')),
                ('is_makeup', models.BooleanField(default=False, help_text='是否补考', verbose_name='是否补考')),
                ('count', models.IntegerField(verbose_name='补考次数')),
                ('name', models.ForeignKey(help_text='统计表名称', on_delete=django.db.models.deletion.CASCADE, to='forms.forms', verbose_name='统计表名称')),
                ('user', models.ManyToManyField(help_text='用户', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '统计表',
                'verbose_name_plural': '统计表',
                'db_table': 'table_report',
            },
        ),
    ]