# Generated by Django 3.2 on 2023-02-17 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrCodePlugin', '0019_alter_qrcodeurlpost_uuid_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcodeurlpost',
            name='page_url',
            field=models.CharField(blank=True, choices=[('my-new-blog', 'My new blog'), ('my-second-blog', 'My second blog'), ('my-third-blog', 'My third blog')], max_length=20),
        ),
    ]