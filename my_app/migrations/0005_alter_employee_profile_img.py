# Generated by Django 4.2.3 on 2023-08-17 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_alter_employee_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_img',
            field=models.FileField(default='anonymous.jpg', max_length=250, upload_to='profile/'),
        ),
    ]
