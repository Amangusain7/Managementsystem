# Generated by Django 3.1.6 on 2021-02-27 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managetask', '0006_auto_20210227_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertask',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='usertask',
            old_name='updated_at',
            new_name='updated',
        ),
    ]
