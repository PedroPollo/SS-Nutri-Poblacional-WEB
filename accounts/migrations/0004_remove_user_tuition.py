# Generated by Django 4.2.2 on 2023-08-22 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="tuition",
        ),
    ]
