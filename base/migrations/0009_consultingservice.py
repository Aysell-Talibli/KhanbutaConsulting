# Generated by Django 4.2.3 on 2023-08-03 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_apply_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultingService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('image', models.TextField()),
            ],
        ),
    ]