# Generated by Django 4.2 on 2023-05-16 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fresh", "0021_checkout_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="checkout",
            name="state",
            field=models.CharField(max_length=50, null=True),
        ),
    ]