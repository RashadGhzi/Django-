# Generated by Django 4.1.3 on 2022-12-19 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0003_booksadd_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksadd',
            name='book_desc',
            field=models.CharField(max_length=120),
        ),
    ]