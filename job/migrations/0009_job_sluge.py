# Generated by Django 3.1.3 on 2020-12-04 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_auto_20201203_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='sluge',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
