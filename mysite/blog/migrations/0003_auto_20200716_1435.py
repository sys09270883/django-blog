# Generated by Django 3.0.8 on 2020-07-16 05:35

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownx.models.MarkdownxField(verbose_name='CONTENT'),
        ),
    ]
