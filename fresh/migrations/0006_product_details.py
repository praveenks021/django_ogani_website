# Generated by Django 4.2 on 2023-05-05 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("fresh", "0005_alter_product_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product_details",
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
                ("details", models.CharField(max_length=500)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="fresh.product"
                    ),
                ),
            ],
        ),
    ]
