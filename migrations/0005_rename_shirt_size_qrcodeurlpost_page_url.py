# Generated by Django 3.2 on 2023-02-12 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qrCodePlugin', '0004_qrcodeurlpost_shirt_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='qrcodeurlpost',
            old_name='shirt_size',
            new_name='page_url',
        ),
    ]
