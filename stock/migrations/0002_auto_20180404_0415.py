# Generated by Django 2.0.3 on 2018-04-04 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='item_name',
            new_name='item',
        ),
    ]
