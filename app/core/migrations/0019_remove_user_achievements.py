# Generated by Django 3.1.4 on 2020-12-29 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_user_achievements'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='achievements',
        ),
    ]