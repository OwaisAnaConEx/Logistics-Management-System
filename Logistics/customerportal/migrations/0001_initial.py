# Generated by Django 4.1.3 on 2022-11-27 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("city", models.CharField(max_length=120)),
                ("province", models.CharField(max_length=120)),
                ("state", models.CharField(max_length=120)),
                ("address", models.TextField()),
                ("postal", models.IntegerField()),
                ("contact", models.IntegerField()),
                ("cnic", models.IntegerField()),
                (
                    "userid",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ServiceType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
                ("charges", models.FloatField(max_length=120)),
                ("estimateTime", models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name="Status",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name="Rider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
                ("lname", models.CharField(max_length=120)),
                ("contact", models.IntegerField()),
                ("cnic", models.IntegerField()),
                (
                    "user_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Parcel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("weight", models.IntegerField()),
                ("qty", models.IntegerField()),
                ("destination", models.CharField(max_length=120)),
                ("city", models.CharField(max_length=120)),
                ("province", models.CharField(max_length=120)),
                ("total", models.FloatField(max_length=120)),
                ("consigneeName", models.CharField(max_length=120)),
                ("contact", models.IntegerField()),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customerportal.customer",
                    ),
                ),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customerportal.servicetype",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customerportal.status",
                    ),
                ),
            ],
        ),
    ]
