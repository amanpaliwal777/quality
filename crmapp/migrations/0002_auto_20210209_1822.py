# Generated by Django 3.1.5 on 2021-02-09 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client_services',
            name='quatation_title',
        ),
        migrations.AlterField(
            model_name='client_services',
            name='quatation',
            field=models.FileField(null=True, upload_to='media'),
        ),
    ]
