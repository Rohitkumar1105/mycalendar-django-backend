# Generated by Django 2.2 on 2020-06-25 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytasks', '0002_auto_20200625_1056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mytasks',
            old_name='content',
            new_name='task_content',
        ),
        migrations.RemoveField(
            model_name='mytasks',
            name='id',
        ),
        migrations.AddField(
            model_name='mytasks',
            name='task_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
