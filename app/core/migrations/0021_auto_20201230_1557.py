# Generated by Django 3.1.4 on 2020-12-30 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20201230_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='rewards',
            field=models.ManyToManyField(blank=True, to='core.Reward'),
        ),
    ]