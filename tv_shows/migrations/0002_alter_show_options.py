# Generated by Django 3.2.6 on 2021-08-24 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='show',
            options={'ordering': ('id',)},
        ),
    ]
