# Generated by Django 3.0.3 on 2020-09-24 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edits', '0004_auto_20200924_0453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='edit',
            old_name='url',
            new_name='video',
        ),
    ]