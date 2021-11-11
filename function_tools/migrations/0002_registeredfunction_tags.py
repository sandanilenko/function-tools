# Generated by Django 2.2.4 on 2021-10-26 23:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('function_tools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredfunction',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=128), default=list, size=None),
        ),
    ]