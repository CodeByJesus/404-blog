# Generated by Django 5.2.4 on 2025-07-23 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_is_pinned'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [('can_post', 'Can post new articles')], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
