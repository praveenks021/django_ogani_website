# Generated by Django 4.2 on 2023-05-24 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fresh", "0028_featured_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="featured",
            name="url",
        ),
    ]