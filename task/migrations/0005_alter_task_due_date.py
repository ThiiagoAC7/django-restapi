# Generated by Django 4.2.14 on 2024-08-03 03:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 3, 3, 53, 48, 374360, tzinfo=datetime.timezone.utc)),
        ),
    ]
