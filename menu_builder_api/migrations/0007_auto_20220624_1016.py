# Generated by Django 3.2.13 on 2022-06-24 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_builder_api', '0006_rename_menu_items_section'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modifiers',
            old_name='description',
            new_name='Modifiers_description',
        ),
        migrations.AlterField(
            model_name='modifiers',
            name='items',
            field=models.ManyToManyField(to='menu_builder_api.Items'),
        ),
    ]