# Generated by Django 5.0.1 on 2024-06-23 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hold', '0012_alter_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
