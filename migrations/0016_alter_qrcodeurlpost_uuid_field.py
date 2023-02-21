# Generated by Django 3.2 on 2023-02-14 14:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('qrCodePlugin', '0015_alter_qrcodeurlpost_uuid_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcodeurlpost',
            name='uuid_field',
            field=models.UUIDField(default=uuid.UUID('0290afa2-4fa7-4a8e-80f5-04dc136faca2'), editable=False),
        ),
    ]
