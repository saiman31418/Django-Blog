# Generated by Django 3.2.3 on 2022-02-18 05:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='posts',
            name='aurt',
            field=models.CharField(default=True, max_length=15),
        ),
        migrations.AddField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.TextField(),
        ),
    ]
