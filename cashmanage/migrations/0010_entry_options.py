# Generated by Django 2.2.1 on 2019-05-16 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashmanage', '0009_auto_20190516_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='options',
            field=models.CharField(default='2', max_length=2),
        ),
    ]