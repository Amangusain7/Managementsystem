# Generated by Django 3.1.6 on 2021-02-22 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0003_auto_20210222_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('1', 'Male'), ('2', 'female')], max_length=100, null=True),
        ),
    ]
