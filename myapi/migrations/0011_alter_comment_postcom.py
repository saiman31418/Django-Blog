# Generated by Django 3.2.3 on 2022-02-23 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0010_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='postcom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myapi.posts'),
        ),
    ]
