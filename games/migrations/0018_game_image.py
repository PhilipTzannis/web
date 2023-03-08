# Generated by Django 3.0.8 on 2020-08-26 15:22

from django.db import migrations, models

import games.models


class Migration(migrations.Migration):
    dependencies = [
        ("games", "0017_auto_20200806_1941"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=games.models.get_game_image_name
            ),
        ),
    ]
