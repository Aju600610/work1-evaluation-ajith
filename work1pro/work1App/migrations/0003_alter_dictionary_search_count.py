# Generated by Django 4.2.6 on 2023-10-08 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work1App', '0002_alter_dictionary_search_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionary',
            name='search_count',
            field=models.IntegerField(),
        ),
    ]
