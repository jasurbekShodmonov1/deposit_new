# Generated by Django 5.0.6 on 2024-06-06 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='prediction',
            field=models.CharField(max_length=100),
        ),
    ]
