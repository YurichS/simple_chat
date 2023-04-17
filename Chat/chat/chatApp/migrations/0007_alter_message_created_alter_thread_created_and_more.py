# Generated by Django 4.2 on 2023-04-17 11:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0006_alter_message_created_alter_message_sender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 17, 11, 24, 43, 541118, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 17, 11, 24, 43, 540451, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='updated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 17, 11, 24, 43, 540462, tzinfo=datetime.timezone.utc)),
        ),
    ]