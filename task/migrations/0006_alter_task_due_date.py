# Generated by Django 4.2.14 on 2024-08-03 04:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 3, 4, 44, 17, 432921, tzinfo=datetime.timezone.utc)),
        ),
    ]
