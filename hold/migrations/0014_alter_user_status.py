# Generated by Django 5.0.1 on 2024-06-25 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hold', '0013_alter_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]
