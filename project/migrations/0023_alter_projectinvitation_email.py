# Generated by Django 3.2.19 on 2023-05-17 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0022_projectinvitation_consumed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinvitation',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]