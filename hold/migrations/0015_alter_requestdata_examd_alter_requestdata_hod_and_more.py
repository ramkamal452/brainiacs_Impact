# Generated by Django 5.0.1 on 2024-06-27 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hold', '0014_alter_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestdata',
            name='examD',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='requestdata',
            name='hoD',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='requestdata',
            name='hostelD',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='requestdata',
            name='labD',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='requestdata',
            name='libD',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='requestdata',
            name='secD',
            field=models.CharField(max_length=100),
        ),
    ]
