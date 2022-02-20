# Generated by Django 3.2.3 on 2022-02-14 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flightid', models.IntegerField()),
                ('destination', models.CharField(max_length=40)),
                ('distance', models.IntegerField()),
                ('fuelquantity', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
