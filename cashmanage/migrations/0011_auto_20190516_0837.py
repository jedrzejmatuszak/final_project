# Generated by Django 2.2.1 on 2019-05-16 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashmanage', '0010_entry_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='options',
            field=models.TextField(choices=[('1', 'Wpływ'), ('2', 'Wydatek'), ('3', 'Przeksięgowanie')], default='2'),
        ),
    ]
