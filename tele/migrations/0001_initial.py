# Generated by Django 4.1.7 on 2023-03-02 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='consultantDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user_name', models.CharField(max_length=30, unique=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('speciality', models.CharField(max_length=30)),
                ('qualification', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='farmerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user_name', models.CharField(max_length=30, unique=True)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
