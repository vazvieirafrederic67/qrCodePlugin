# Generated by Django 3.2 on 2023-02-16 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrCodePlugin', '0018_alter_qrcodeurlpost_uuid_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcodeurlpost',
            name='uuid_field',
            field=models.UUIDField(blank=True, editable=False),
        ),
    ]