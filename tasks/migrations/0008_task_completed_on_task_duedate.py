# Generated by Django 4.2.1 on 2023-06-06 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_remove_task_completed_on_remove_task_duedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='dueDate',
            field=models.DateTimeField(null=True),
        ),
    ]
