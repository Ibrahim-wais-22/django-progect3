# Generated by Django 3.1.3 on 2020-12-04 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_auto_20201204_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
