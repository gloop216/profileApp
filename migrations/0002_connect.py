# Generated by Django 5.0.1 on 2024-05-31 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=1000)),
                ('msg', models.TextField(max_length=2000)),
            ],
        ),
    ]
