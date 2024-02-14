# Generated by Django 5.0 on 2024-02-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('newapp', '0002_delete_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=500)),
            ],
        ),
    ]
