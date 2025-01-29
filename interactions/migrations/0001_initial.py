# Generated by Django 5.1.4 on 2025-01-13 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=45)),
                ('reason', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='StatusServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=45)),
                ('comment', models.CharField(max_length=150)),
                ('dateupdated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('datecreated', models.DateTimeField(auto_now_add=True)),
                ('disponibility', models.CharField(max_length=45)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.services')),
            ],
        ),
    ]
