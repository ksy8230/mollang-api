# Generated by Django 4.0.6 on 2022-07-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='categories',
            field=models.JSONField(default='{}'),
        ),
    ]
