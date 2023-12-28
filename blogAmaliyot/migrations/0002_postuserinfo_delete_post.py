# Generated by Django 5.0 on 2023-12-27 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogAmaliyot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostUserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('familiya', models.CharField(max_length=100)),
                ('telefon', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('xabar', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]