# Generated by Django 5.0.6 on 2024-06-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_track'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='duration',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
