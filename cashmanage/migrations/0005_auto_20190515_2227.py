# Generated by Django 2.2.1 on 2019-05-15 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cashmanage', '0004_accountbalance_subcategory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AccountBalance',
            new_name='Entry',
        ),
    ]