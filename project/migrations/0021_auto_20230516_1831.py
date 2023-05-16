# Generated by Django 3.2.19 on 2023-05-16 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0020_alter_managementteam_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_team',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='équipe_projet', to='project.projectteam'),
        ),
        migrations.AlterField(
            model_name='project',
            name='équipe_encadrement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='équipe_encadrement', to='project.managementteam'),
        ),
    ]
