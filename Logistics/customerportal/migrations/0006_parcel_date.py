# Generated by Django 4.1.3 on 2022-12-09 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customerportal", "0005_rename_province_parcel_state"),
    ]

    operations = [
        migrations.AddField(
            model_name="parcel",
            name="date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
