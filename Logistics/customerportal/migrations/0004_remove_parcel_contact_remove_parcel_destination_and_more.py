# Generated by Django 4.1.3 on 2022-12-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "customerportal",
            "0003_parcel_consigneecontact_parcel_consigneeemail_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="parcel",
            name="contact",
        ),
        migrations.RemoveField(
            model_name="parcel",
            name="destination",
        ),
        migrations.AddField(
            model_name="parcel",
            name="PaymentStatus",
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name="parcel",
            name="country",
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name="parcel",
            name="deliverlocation",
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="parcel",
            name="pickuplocation",
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="parcel",
            name="city",
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name="parcel",
            name="consigneeContact",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="parcel",
            name="province",
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name="parcel",
            name="total",
            field=models.FloatField(max_length=120, null=True),
        ),
    ]
