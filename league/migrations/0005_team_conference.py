# Generated by Django 4.2.1 on 2023-07-05 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league', '0004_team_userteam_alter_player_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='conference',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
