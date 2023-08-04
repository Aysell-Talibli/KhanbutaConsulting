# Generated by Django 4.2.3 on 2023-08-03 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_about_aboutdetailed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='openinghours',
            name='closing_time',
        ),
        migrations.RemoveField(
            model_name='openinghours',
            name='opening_time',
        ),
        migrations.AddField(
            model_name='openinghours',
            name='time',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.service')),
            ],
        ),
    ]
