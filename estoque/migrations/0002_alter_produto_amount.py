# Generated by Django 5.1.4 on 2024-12-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("estoque", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="amount",
            field=models.IntegerField(),
        ),
    ]
