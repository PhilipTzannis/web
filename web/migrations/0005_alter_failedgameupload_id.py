# Generated by Django 3.2 on 2021-04-13 16:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0004_failedgameupload_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="failedgameupload",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
