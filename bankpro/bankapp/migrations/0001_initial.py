# Generated by Django 5.0 on 2023-12-20 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='mainimage')),
                ('heading', models.CharField(max_length=250)),
                ('desc', models.TextField(default=True)),
            ],
        ),
    ]
