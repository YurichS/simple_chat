# Generated by Django 4.2 on 2023-04-15 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0002_thread_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 15, 19, 8, 40, 650260, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 15, 19, 8, 40, 649952, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 15, 19, 8, 40, 650021, tzinfo=datetime.timezone.utc)),
        ),
    ]
