# Generated by Django 5.1.4 on 2025-01-30 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='services',
            name='duration',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='services',
            name='tags',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='services',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
