# Generated by Django 3.1.3 on 2020-11-26 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_achievement'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAchievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField()),
                ('achievement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.achievement')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
