# Generated by Django 4.1 on 2023-09-02 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="date",
            field=models.DateField(default="1999-02-01"),
            preserve_default=False,
        ),
    ]
