# Generated by Django 3.1.3 on 2020-11-26 17:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_reward_studentreward'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
