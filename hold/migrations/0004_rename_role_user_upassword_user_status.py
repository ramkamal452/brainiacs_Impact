# Generated by Django 5.0.1 on 2024-06-16 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hold', '0003_remove_user_id_alter_user_uid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='role',
            new_name='upassword',
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
