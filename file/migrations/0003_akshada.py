# Generated by Django 5.0.3 on 2024-04-20 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_learn'),
    ]

    operations = [
        migrations.CreateModel(
            name='Akshada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=255)),
                ('aemail', models.CharField(max_length=255)),
                ('aissue', models.CharField(max_length=255)),
                ('aremark', models.CharField(max_length=255)),
                ('aservice', models.CharField(max_length=255)),
            ],
        ),
    ]
