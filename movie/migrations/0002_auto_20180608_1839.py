# Generated by Django 2.0.6 on 2018-06-08 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='upload_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]