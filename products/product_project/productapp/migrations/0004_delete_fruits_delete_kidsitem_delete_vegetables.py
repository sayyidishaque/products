# Generated by Django 4.2 on 2023-04-27 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0003_remove_fruits_name_remove_kidsitem_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='fruits',
        ),
        migrations.DeleteModel(
            name='kidsitem',
        ),
        migrations.DeleteModel(
            name='vegetables',
        ),
    ]
