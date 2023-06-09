# Generated by Django 3.2.18 on 2023-04-30 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_alter_projectvalidation_committee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectvalidation',
            name='decision',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_decision', to='project.decisionofcommittee'),
        ),
    ]
