# Generated by Django 3.2.18 on 2023-04-30 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0013_alter_project_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectvalidation',
            name='committee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_validation_committe', to='project.validationcommittee'),
        ),
    ]
