# Generated by Django 4.0.5 on 2022-09-24 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='prof',
            new_name='image',
        ),
    ]
