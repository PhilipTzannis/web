# Generated by Django 2.2.4 on 2019-09-02 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("games", "0007_auto_20190812_0258")]

    operations = [
        migrations.AddField(
            model_name="game", name="dnf", field=models.BooleanField(default=False)
        )
    ]
