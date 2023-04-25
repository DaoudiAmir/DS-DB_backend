# Generated by Django 3.2.18 on 2023-04-25 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
        ('project', '0002_auto_20230423_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('On Hold', 'On Hold'), ('Rejected', 'Rejected')], default='On Hold', max_length=50)),
                ('deadline', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project_leader', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('supervisors', models.ManyToManyField(related_name='supervisors', to='core.Teacher')),
            ],
        ),
    ]
