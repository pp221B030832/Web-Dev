# Generated by Django 4.1.7 on 2023-04-12 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.TextField(default='Atyrau'),
        ),
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='description',
            field=models.TextField(default='None'),
        ),
    ]