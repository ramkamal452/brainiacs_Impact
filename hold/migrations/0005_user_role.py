# Generated by Django 5.0.1 on 2024-06-18 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hold', '0004_rename_role_user_upassword_user_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
