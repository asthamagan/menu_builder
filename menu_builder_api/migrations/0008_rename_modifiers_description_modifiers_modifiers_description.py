# Generated by Django 3.2.13 on 2022-06-24 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_builder_api', '0007_auto_20220624_1016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modifiers',
            old_name='Modifiers_description',
            new_name='modifiers_description',
        ),
    ]