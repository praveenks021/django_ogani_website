# Generated by Django 4.2 on 2023-05-03 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fresh", "0004_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(null=True, upload_to="media/"),
        ),
    ]
