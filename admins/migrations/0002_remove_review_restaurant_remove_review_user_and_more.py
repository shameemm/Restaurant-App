# Generated by Django 5.0 on 2023-12-24 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.DeleteModel(
            name='Bookmark',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
