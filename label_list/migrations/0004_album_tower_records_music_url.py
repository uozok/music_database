# Generated by Django 3.2.22 on 2023-10-29 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('label_list', '0003_auto_20231027_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='tower_records_music_url',
            field=models.URLField(blank=True),
        ),
    ]
