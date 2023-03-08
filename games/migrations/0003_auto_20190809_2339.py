# Generated by Django 2.2.4 on 2019-08-09 23:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("games", "0002_auto_20190806_0020")]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="players",
            field=models.ManyToManyField(
                related_name="games",
                through="games.GamePlayer",
                to=settings.AUTH_USER_MODEL,
            ),
        )
    ]
