# Generated by Django 3.2.8 on 2022-05-20 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_backup_payroll_payroll_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='backup_payroll',
            name='anio',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='backup_payroll',
            name='month',
            field=models.CharField(default='', max_length=15),
        ),
    ]
