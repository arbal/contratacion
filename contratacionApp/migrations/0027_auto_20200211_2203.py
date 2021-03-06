# Generated by Django 2.2.5 on 2020-02-12 03:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratacionApp', '0026_auto_20200108_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentcontract',
            name='numberRegistration',
            field=models.CharField(default=0, max_length=250, verbose_name='Número de Registro'),
        ),
        migrations.AddField(
            model_name='privatecontract',
            name='numberRegistration',
            field=models.CharField(default=0, max_length=250, verbose_name='Número de Registro'),
        ),
        migrations.AlterField(
            model_name='auditcurrentcontract',
            name='newEndDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 22, 3, 13, 864505), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='auditcurrentcontract',
            name='newStartDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 22, 3, 13, 864505), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='auditprivatecontract',
            name='newEndDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 22, 3, 13, 866504), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='auditprivatecontract',
            name='newStartDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 22, 3, 13, 866504), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='currentcontract',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 22, 3, 13, 869501), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='currentcontract',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 22, 3, 13, 869501), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='currentcontract',
            name='supplement',
            field=models.ManyToManyField(blank=True, max_length=250, null=True, to='contratacionApp.Supplement', verbose_name='Suplemento'),
        ),
        migrations.AlterField(
            model_name='privatecontract',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 22, 3, 13, 871500), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='privatecontract',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 11, 22, 3, 13, 871500), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='privatecontract',
            name='supplement',
            field=models.ManyToManyField(blank=True, max_length=250, null=True, to='contratacionApp.Supplement', verbose_name='Suplemento'),
        ),
    ]
