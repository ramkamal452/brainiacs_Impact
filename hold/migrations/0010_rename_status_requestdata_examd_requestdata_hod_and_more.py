# Generated by Django 5.0.1 on 2024-06-23 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hold', '0009_alter_user_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestdata',
            old_name='status',
            new_name='examD',
        ),
        migrations.AddField(
            model_name='requestdata',
            name='hoD',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='requestdata',
            name='hostelD',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='requestdata',
            name='labD',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='requestdata',
            name='libD',
            field=models.BooleanField(default=False),
        ),
    ]
