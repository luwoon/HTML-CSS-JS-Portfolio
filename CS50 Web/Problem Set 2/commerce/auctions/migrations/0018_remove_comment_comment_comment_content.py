# Generated by Django 4.2.11 on 2024-07-18 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0017_rename_commenter_comment_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="comment",
        ),
        migrations.AddField(
            model_name="comment",
            name="content",
            field=models.TextField(default=""),
        ),
    ]
