# Generated by Django 4.1.7 on 2023-03-07 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentRegister',
            new_name='Student',
        ),
    ]
