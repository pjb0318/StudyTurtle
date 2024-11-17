# Generated by Django 5.1.3 on 2024-11-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_task_is_complete_alter_task_assigned_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='student_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]