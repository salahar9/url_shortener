# Generated by Django 3.2.6 on 2021-10-17 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_alter_shorturl_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorturl',
            name='visits',
        ),
        migrations.AddField(
            model_name='shorturl',
            name='number_of_visits',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=4)),
                ('date_of_visit', models.DateTimeField(auto_now=True)),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='shortener.shorturl')),
            ],
        ),
    ]
