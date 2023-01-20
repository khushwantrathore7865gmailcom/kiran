# Generated by Django 4.1.3 on 2023-01-12 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_customization_inquiry_requestforsample"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("email", models.EmailField(max_length=254)),
                ("first_name", models.CharField(max_length=250)),
                ("last_name", models.CharField(max_length=250)),
                ("phone", models.CharField(max_length=15)),
                ("desc", models.TextField()),
                ("date", models.DateTimeField()),
                ("company", models.CharField(max_length=250)),
                ("designation", models.CharField(max_length=250)),
                ("country", models.CharField(max_length=250)),
            ],
        ),
    ]
