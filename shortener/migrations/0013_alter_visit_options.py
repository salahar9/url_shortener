# Generated by Django 3.2.6 on 2021-10-18 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0012_rename_device_visit_os'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visit',
            options={'verbose_name': 'Link stat', 'verbose_name_plural': 'Stats'},
        ),
    ]