# Generated by Django 4.1 on 2022-09-25 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_alter_forms_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='points',
            old_name='point',
            new_name='points',
        ),
    ]