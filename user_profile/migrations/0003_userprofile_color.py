# Generated by Django 3.0.5 on 2020-05-23 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_userprofile_profession'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='color',
            field=models.CharField(default='green', max_length=10),
        ),
    ]
