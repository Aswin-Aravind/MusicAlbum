# Generated by Django 5.0.6 on 2024-06-10 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='track',
        ),
    ]