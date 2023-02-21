# Generated by Django 3.2 on 2023-02-12 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrCodePlugin', '0003_alter_qrcodeurlpost_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcodeurlpost',
            name='shirt_size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]