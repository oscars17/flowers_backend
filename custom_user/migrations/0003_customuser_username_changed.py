# Generated by Django 3.0.7 on 2020-06-28 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0002_passwordrestorationtoken_registrationtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username_changed',
            field=models.BooleanField(default=False),
        ),
    ]
