# Generated by Django 4.1.1 on 2022-10-06 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games_app', '0002_platform_game_platform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='game',
            name='platform',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='games_app.platform'),
        ),
        migrations.AddField(
            model_name='game',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='games_app.category'),
        ),
    ]
