# Generated by Django 3.2 on 2023-02-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrCodePlugin', '0010_qrcodeurlpost_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcodeurlpost',
            name='created_at',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
