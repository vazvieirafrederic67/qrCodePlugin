# Generated by Django 3.2 on 2023-02-14 14:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('qrCodePlugin', '0016_alter_qrcodeurlpost_uuid_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcodeurlpost',
            name='uuid_field',
            field=models.UUIDField(auto_created=uuid.UUID('1e77cff5-74c0-4f1f-b2c6-28ebb76f2f4a'), editable=False),
        ),
    ]
