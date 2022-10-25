# Generated by Django 4.0.6 on 2022-08-24 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='static/')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10000)),
                ('image', models.ImageField(upload_to='static/')),
                ('description', models.CharField(max_length=5000)),
                ('location', models.CharField(max_length=10900)),
                ('type', models.CharField(max_length=290)),
            ],
        ),
        migrations.CreateModel(
            name='Politics',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='static/')),
                ('name', models.CharField(max_length=1000)),
                ('position', models.CharField(max_length=500)),
                ('about_khadpu', models.CharField(max_length=10000)),
                ('facebook', models.CharField(max_length=10000)),
            ],
        ),
    ]
