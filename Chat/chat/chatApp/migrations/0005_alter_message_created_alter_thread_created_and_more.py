# Generated by Django 4.2 on 2023-04-15 20:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0004_alter_message_created_alter_thread_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 15, 20, 27, 55, 973190, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 15, 20, 27, 55, 972505, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 15, 20, 27, 55, 972515, tzinfo=datetime.timezone.utc)),
        ),
    ]
