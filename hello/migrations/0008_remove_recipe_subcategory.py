# Generated by Django 4.2.11 on 2024-03-21 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_alter_recipe_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='subcategory',
        ),
    ]