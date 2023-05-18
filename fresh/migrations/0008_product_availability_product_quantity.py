# Generated by Django 4.2 on 2023-05-08 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fresh", "0007_product_description_delete_product_details"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="availability",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="quantity",
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
