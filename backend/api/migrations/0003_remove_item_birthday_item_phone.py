# Generated by Django 4.2.13 on 2024-07-06 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_item_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='birthday',
        ),
        migrations.AddField(
            model_name='item',
            name='phone',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
