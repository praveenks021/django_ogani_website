# Generated by Django 4.2 on 2023-05-16 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fresh", "0020_remove_checkout_cart"),
    ]

    operations = [
        migrations.AddField(
            model_name="checkout",
            name="country",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
