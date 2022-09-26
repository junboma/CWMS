# Generated by Django 4.1 on 2022-09-26 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0009_alter_points_points'),
        ('report', '0007_reason_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reason',
            name='points',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='关联扣分点', null=True, on_delete=django.db.models.deletion.PROTECT, to='forms.points', verbose_name='关联扣分点'),
        ),
    ]