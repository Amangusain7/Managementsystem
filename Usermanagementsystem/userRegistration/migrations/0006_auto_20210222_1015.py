# Generated by Django 3.1.6 on 2021-02-22 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0005_user_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='avatar',
            new_name='profile_image',
        ),
    ]
