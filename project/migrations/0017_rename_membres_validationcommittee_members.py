# Generated by Django 3.2.18 on 2023-05-02 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_rename_decription_decisionofcommittee_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='validationcommittee',
            old_name='membres',
            new_name='members',
        ),
    ]
