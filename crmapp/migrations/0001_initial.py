# Generated by Django 3.1.5 on 2021-02-08 12:28

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
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('client_business', models.CharField(max_length=200)),
                ('client_phone', models.BigIntegerField()),
                ('client_email', models.EmailField(max_length=100)),
                ('client_address', models.CharField(max_length=300)),
                ('client_country', models.CharField(max_length=20)),
                ('client_work_description', models.CharField(max_length=300)),
                ('client_created', models.DateTimeField()),
                ('superuser_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client_Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services', models.CharField(max_length=200)),
                ('pricing', models.IntegerField()),
                ('due', models.IntegerField()),
                ('advance', models.IntegerField()),
                ('quatation_title', models.CharField(max_length=100)),
                ('quatation', models.FileField(upload_to='media')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmapp.clients')),
                ('superuser_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client_Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_response', models.CharField(max_length=500)),
                ('client_response_date', models.DateTimeField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmapp.clients')),
                ('superuser_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
