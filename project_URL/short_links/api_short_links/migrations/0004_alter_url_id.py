# Generated by Django 4.2.4 on 2023-09-03 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_short_links', '0003_alter_url_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
