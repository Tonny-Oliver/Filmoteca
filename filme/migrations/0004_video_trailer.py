# Generated by Django 5.0.1 on 2024-02-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0003_alter_video_filme'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='trailer',
            field=models.URLField(default='Null'),
            preserve_default=False,
        ),
    ]
