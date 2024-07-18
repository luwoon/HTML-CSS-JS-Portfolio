# Generated by Django 4.2.11 on 2024-07-06 03:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0003_alter_listing_created_time"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bid",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("amt", models.DecimalField(decimal_places=2, max_digits=10)),
                ("time", models.DateTimeField(auto_now_add=True)),
                (
                    "bidder",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bids",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("time", models.DateTimeField(auto_now_add=True)),
                (
                    "commenter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Bids",
        ),
        migrations.DeleteModel(
            name="Comments",
        ),
        migrations.RemoveField(
            model_name="listing",
            name="username",
        ),
        migrations.AddField(
            model_name="listing",
            name="details",
            field=models.CharField(default="", max_length=2000),
        ),
        migrations.AddField(
            model_name="listing",
            name="image",
            field=models.ImageField(default="", upload_to="listings/"),
        ),
        migrations.AddField(
            model_name="listing",
            name="posted_by",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="listings",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="created_time",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="listing",
            name="title",
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name="comment",
            name="listing_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="auctions.listing",
            ),
        ),
        migrations.AddField(
            model_name="bid",
            name="listing_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bids",
                to="auctions.listing",
            ),
        ),
    ]
