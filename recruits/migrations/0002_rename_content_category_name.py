# Generated by Django 4.1 on 2022-08-25 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruits', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='content',
            new_name='name',
        ),
    ]
