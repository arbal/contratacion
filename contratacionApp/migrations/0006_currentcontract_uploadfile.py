# Generated by Django 2.2.5 on 2019-10-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratacionApp', '0005_auto_20190927_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentcontract',
            name='upLoadFile',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
