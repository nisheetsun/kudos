# Generated by Django 3.1 on 2020-08-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200813_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='content',
            name='content',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='content',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]