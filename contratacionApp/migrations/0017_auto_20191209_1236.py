# Generated by Django 2.2.5 on 2019-12-09 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratacionApp', '0016_auto_20191209_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditcurrentcontract',
            name='newEndDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 12, 36, 35, 372402), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='auditcurrentcontract',
            name='newStartDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 12, 36, 35, 372357), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='auditprivatecontract',
            name='ciNumber',
            field=models.CharField(blank=True, max_length=11, verbose_name='Carnet Identidad'),
        ),
        migrations.AlterField(
            model_name='auditprivatecontract',
            name='newEndDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 12, 36, 35, 374283), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='auditprivatecontract',
            name='newStartDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 12, 36, 35, 374235), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='currentcontract',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 12, 36, 35, 375729), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='currentcontract',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 12, 36, 35, 375691), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='privatecontract',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 12, 36, 35, 377227), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='privatecontract',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 9, 12, 36, 35, 377189), verbose_name='Fecha Inicio'),
        ),
    ]