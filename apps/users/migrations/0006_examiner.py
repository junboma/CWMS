# Generated by Django 4.1 on 2022-09-25 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_userprofile_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examiner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort', models.IntegerField(default=1, help_text='考评人顺序', verbose_name='考评人顺序')),
                ('name', models.ForeignKey(db_constraint=False, help_text='考评人', on_delete=django.db.models.deletion.CASCADE, to='users.userprofile', verbose_name='考评人')),
            ],
            options={
                'verbose_name': '考评人管理',
                'verbose_name_plural': '考评人管理',
                'db_table': 'system_examiner',
                'ordering': ('sort',),
            },
        ),
    ]
