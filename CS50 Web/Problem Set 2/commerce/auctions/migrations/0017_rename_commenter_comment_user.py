# Generated by Django 4.2.11 on 2024-07-18 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0016_bid_time_alter_bid_listing_id_alter_bid_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="commenter",
            new_name="user",
        ),
    ]
