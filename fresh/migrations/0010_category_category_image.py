# Generated by Django 4.2 on 2023-05-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fresh", "0009_alter_product_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="category_image",
            field=models.ImageField(null=True, upload_to="media/"),
        ),
    ]
