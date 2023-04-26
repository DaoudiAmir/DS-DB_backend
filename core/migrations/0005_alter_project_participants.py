# Generated by Django 3.2.18 on 2023-04-26 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_project_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='participants',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
