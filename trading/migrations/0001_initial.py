# Generated by Django 5.1.1 on 2024-09-29 17:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ChartType",
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
                ("name", models.CharField(max_length=50, unique=True)),
                ("symbol", models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Candle",
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
                ("time", models.DateTimeField()),
                ("open_price", models.FloatField()),
                ("close_price", models.FloatField()),
                ("min_price", models.FloatField()),
                ("max_price", models.FloatField()),
                (
                    "chart_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trading.charttype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Bet",
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
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "prediction",
                    models.CharField(
                        choices=[("UP", "Up"), ("DOWN", "Down")], max_length=10
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "result",
                    models.CharField(
                        choices=[
                            ("WIN", "Win"),
                            ("LOSS", "Loss"),
                            ("PENDING", "Pending"),
                        ],
                        default="PENDING",
                        max_length=10,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "chart_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="trading.charttype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                (
                    "balance",
                    models.DecimalField(
                        decimal_places=2, default=1000.0, max_digits=10
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
