# Generated by Django 4.2.4 on 2023-09-03 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_short_links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(max_length=7),
        ),
    ]