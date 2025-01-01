# Generated by Django 2.2.28 on 2023-05-31 13:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_auto_20230531_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date (Morocco)')),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated Date (Morocco)')),
            ],
        ),
    ]
