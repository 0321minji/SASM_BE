# Generated by Django 4.0 on 2023-04-01 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_rename_is_authorized_user_is_verified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_sdp',
            new_name='is_sdp_admin',
        ),
    ]