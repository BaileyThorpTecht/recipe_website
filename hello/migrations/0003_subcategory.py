# Generated by Django 4.2.11 on 2024-03-21 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('parent_category', models.CharField(max_length=100)),
            ],
        ),
    ]
