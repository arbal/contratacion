# Generated by Django 2.2.5 on 2019-12-09 04:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratacionApp', '0012_auto_20191208_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditCurrentContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('userName', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nombre')),
                ('contractNumber', models.CharField(blank=True, max_length=250, null=True, verbose_name='Número de contrato')),
                ('startDate', models.DateTimeField(default=datetime.datetime(2019, 12, 8, 23, 13, 17, 396815), verbose_name='Fecha Inicio')),
                ('endDate', models.DateTimeField(default=datetime.datetime(2019, 12, 8, 23, 13, 17, 396865), verbose_name='Fecha Vence')),
                ('action', models.CharField(blank=True, max_length=250, null=True, verbose_name='accion que realizo')),
            ],
        ),
        migrations.AlterField(
            model_name='currentcontract',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 8, 23, 13, 17, 397732), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='currentcontract',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 8, 23, 13, 17, 397694), verbose_name='Fecha Inicio'),
        ),
        migrations.AlterField(
            model_name='privatecontract',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 8, 23, 13, 17, 399445), verbose_name='Fecha Vence'),
        ),
        migrations.AlterField(
            model_name='privatecontract',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 8, 23, 13, 17, 399405), verbose_name='Fecha Inicio'),
        ),
    ]