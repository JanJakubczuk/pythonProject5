# Generated by Django 4.1.1 on 2022-10-06 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_app', '0004_alter_game_category_gamedetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedetails',
            name='play_time',
            field=models.DurationField(),
        ),
    ]