# Generated by Django 4.1.3 on 2022-11-10 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acc_auth_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authentication',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='authentication',
            old_name='lname',
            new_name='last_name',
        ),
    ]
