# Generated by Django 3.0.2 on 2020-01-26 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generales', '0002_auto_20200122_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='local_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generales.CategoryTeam', verbose_name='local_category'),
        ),
        migrations.AlterField(
            model_name='game',
            name='visitor_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitor_team_category', to='generales.CategoryTeam', verbose_name='visitor_category'),
        ),
        migrations.AlterModelTable(
            name='challenge',
            table='challenge',
        ),
        migrations.AlterModelTable(
            name='challengecomment',
            table='challenge_comment',
        ),
    ]
