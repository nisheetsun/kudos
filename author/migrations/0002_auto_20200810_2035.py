# Generated by Django 3.1 on 2020-08-10 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='alias_name',
            field=models.CharField(blank=True, default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appuser',
            name='bio',
            field=models.CharField(blank=True, default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appuser',
            name='image_url',
            field=models.URLField(blank=True, default=None),
            preserve_default=False,
        ),
    ]