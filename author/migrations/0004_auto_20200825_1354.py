# Generated by Django 3.1 on 2020-08-25 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_auto_20200821_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]