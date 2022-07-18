# Generated by Django 4.0.5 on 2022-07-18 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('categories', models.JSONField()),
                ('region', models.IntegerField()),
                ('phone', models.CharField(max_length=100)),
                ('siteUrl', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
