# Generated by Django 4.2 on 2023-05-16 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fresh", "0018_alter_checkout_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="checkout",
            name="pincode",
            field=models.IntegerField(),
        ),
    ]
