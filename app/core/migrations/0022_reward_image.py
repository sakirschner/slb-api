# Generated by Django 3.1.5 on 2021-01-11 00:11

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20201230_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='reward',
            name='image',
            field=models.ImageField(blank=True, upload_to=core.models.reward_image_file_path),
        ),
    ]