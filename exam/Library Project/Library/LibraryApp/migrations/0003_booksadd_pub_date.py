# Generated by Django 4.1.3 on 2022-12-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0002_booklend_to_date_alter_booksadd_book_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksadd',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
