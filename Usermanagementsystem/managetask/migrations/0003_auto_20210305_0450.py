# Generated by Django 3.1.6 on 2021-03-05 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managetask', '0002_auto_20210305_0437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='subtask',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='managetask.usertask'),
        ),
    ]
