# Generated by Django 2.1 on 2018-10-14 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blog_thumb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='thumb',
            new_name='video',
        ),
    ]
