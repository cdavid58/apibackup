# Generated by Django 3.2.8 on 2022-05-27 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20220520_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='backup_pdfs',
            name='number',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='backup_pdfs',
            name='prefix',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='backup_pdfs',
            name='type_pdf',
            field=models.IntegerField(default=1),
        ),
    ]
