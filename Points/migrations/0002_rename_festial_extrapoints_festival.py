# Generated by Django 4.1 on 2022-09-06 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Points', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extrapoints',
            old_name='festial',
            new_name='festival',
        ),
    ]