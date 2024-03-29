# Generated by Django 2.2.4 on 2021-11-12 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('function_tools', '0002_registeredfunction_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImplementationStrategy',
            fields=[
                ('title', models.TextField(verbose_name='расшифровка значения')),
                ('key', models.CharField(db_index=True, max_length=512, primary_key=True, serialize=False, verbose_name='ключ')),
            ],
            options={
                'verbose_name': 'Стратегия создания функции',
                'db_table': 'function_tools_implementation_strategy',
            },
        ),
    ]
