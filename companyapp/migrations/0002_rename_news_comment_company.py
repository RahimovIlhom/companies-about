# Generated by Django 4.0.3 on 2022-06-15 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companyapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='news',
            new_name='company',
        ),
    ]