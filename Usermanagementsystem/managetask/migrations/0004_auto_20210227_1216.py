# Generated by Django 3.1.6 on 2021-02-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managetask', '0003_auto_20210227_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertask',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='usertask',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
