# Generated by Django 2.2.28 on 2023-05-31 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_remove_event_ticket_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='updated_date',
        ),
    ]
