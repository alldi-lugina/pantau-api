# Generated by Django 2.2 on 2021-04-04 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardingpass', '0002_auto_20210325_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiket',
            name='masker',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='tiket',
            name='suhu',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='tiket',
            name='wajah',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
