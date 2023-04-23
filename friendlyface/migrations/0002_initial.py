# Generated by Django 4.2 on 2023-04-21 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("friendlyface", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="person",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(
                related_name="posts", to="friendlyface.tag"
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
