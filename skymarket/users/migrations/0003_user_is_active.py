# Generated by Django 3.2.6 on 2024-04-10 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20240409_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]