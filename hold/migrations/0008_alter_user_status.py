# Generated by Django 5.0.1 on 2024-06-21 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hold', '0007_requestdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]
