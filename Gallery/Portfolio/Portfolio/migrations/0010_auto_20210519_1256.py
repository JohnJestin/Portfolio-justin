# Generated by Django 3.1.6 on 2021-05-19 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0009_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='caption',
            field=models.TextField(),
        ),
    ]