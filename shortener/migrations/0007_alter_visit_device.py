# Generated by Django 3.2.6 on 2021-10-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0006_visit_device'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='device',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
