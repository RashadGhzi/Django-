# Generated by Django 4.1.3 on 2022-11-29 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]