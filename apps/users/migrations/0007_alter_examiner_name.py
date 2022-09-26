# Generated by Django 4.1 on 2022-09-25 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_examiner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examiner',
            name='name',
            field=models.ForeignKey(db_constraint=False, help_text='考评人', on_delete=django.db.models.deletion.PROTECT, to='users.userprofile', verbose_name='考评人'),
        ),
    ]
