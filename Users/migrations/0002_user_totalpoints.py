# Generated by Django 4.1 on 2022-09-03 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='totalPoints',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Total Points'),
        ),
    ]