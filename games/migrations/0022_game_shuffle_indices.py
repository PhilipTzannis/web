# Generated by Django 3.1.2 on 2020-10-28 21:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("games", "0021_auto_20201028_2232"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="shuffle_indices",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
