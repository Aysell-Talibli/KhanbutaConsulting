# Generated by Django 4.2.3 on 2023-08-03 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_backgroundimage_main_openinghours_socialmedia_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=80)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
