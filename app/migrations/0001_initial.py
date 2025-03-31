# Generated by Django 5.1.7 on 2025-03-19 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('F_name', models.CharField(max_length=30)),
                ('M_name', models.CharField(max_length=30)),
                ('p_no', models.IntegerField()),
                ('course', models.CharField(max_length=50)),
                ('roll', models.IntegerField(unique=True)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
