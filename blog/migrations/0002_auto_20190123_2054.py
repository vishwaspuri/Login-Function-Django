# Generated by Django 2.1.5 on 2019-01-23 15:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 15, 24, 56, 746242, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 23, 15, 24, 56, 745368, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_pic'),
        ),
    ]
