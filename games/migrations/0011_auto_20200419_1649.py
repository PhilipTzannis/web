# Generated by Django 3.0.4 on 2020-04-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("games", "0010_auto_20200218_1717"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gameplayerstat",
            name="chugs",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="gameplayerstat",
            name="value_sum",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
