# Generated by Django 4.2.1 on 2023-06-06 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_task_completed_on_task_duedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dueDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
