# Generated by Django 5.0.3 on 2024-04-03 07:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0002_rename_price_resultdata_max_spend_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="resultdata",
            name="day_of_travel",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="resultdata",
            name="query",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="base.querydata",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="resultdata",
            name="time_of_day",
            field=models.TextField(blank=True, null=True),
        ),
    ]