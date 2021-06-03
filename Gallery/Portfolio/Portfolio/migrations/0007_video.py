# Generated by Django 3.1.6 on 2021-05-19 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0006_auto_20210515_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='Images/video')),
                ('caption', models.CharField(max_length=100)),
            ],
        ),
    ]